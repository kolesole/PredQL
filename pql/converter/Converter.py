from abc import abstractmethod

import duckdb

from relbench.base import Database

from antlr4 import InputStream, CommonTokenStream

from pql.parser.Lexer_PQL import Lexer_PQL
from pql.parser.Parser_PQL import Parser_PQL 
from pql.visitor.PQLVisitor import PQLVisitor

from .utils import build_num_condition, build_str_condition, build_null_condition


class PQLConverter:   
    
    def __init__(self, db: Database) -> None:
        self.db = db
        self.pql_visitor = PQLVisitor()
        self.conn = duckdb.connect()
        for name, table in db.table_dict.items():
            self.conn.register(name, table.df)
    
    
    @abstractmethod
    def convert(self, pql_query : str):
        r"""
        Convert a PQL query string into an executable SQL query and return the result as a Table object.

        The function acts as the main entry point for translating PQL into SQL. 
        It first parses the query, identifies its structural components, constructs
        the corresponding SQL subqueries, executes the final SQL query using DuckDB, 
        and returns the result as a Table instance.

        The function performs the following steps:
            - parses the given PQL query string into a dictionary using parse_query;
            - extracts the for_each clause to determine the base table and primary key;
            - builds conditional subqueries for where, assuming, and predict parts;
            - combines these parts into a final SQL query;
            - executes the SQL query using DuckDB;
            - wraps the resulting DataFrame in a Table object.

        Args
        ----
            `pql_query` : str
                The PQL query string to be converted and executed.

        Returns
        -------
            Table
                A Table object containing the result of the executed SQL query, 
                with columns corresponding to the translated PQL query output.
        """
        
        pass
    

    @abstractmethod
    def build_assuming(self, 
                       query_dict : dict,
                       ptable_name : str, 
                       ppk_name : str,
                       predict_query : str) -> str:
        pass
    

    @abstractmethod
    def build_predict(self, 
                      query_dict : dict,
                      ptable_name : str,  
                      ppk_name : str,
                      for_each_query : str) -> str:
        pass
    

    @abstractmethod
    def build_where(self, 
                    query_dict : dict,
                    ptable_name : str,  
                    ppk_name : str) -> str:
        pass

    
    @abstractmethod
    def build_expr(self, 
                   expr_dict : dict,
                   ptable_name : str,
                   ppk_name : str) -> str:
        pass


    @abstractmethod
    def build_aggregation(self, 
                          aggr_dict : dict,
                          ptable_name : str,  
                          ppk_name : str) -> str:
        pass
        
    
    def parse_query(self, 
                    pql_query : str) -> dict:
        r"""
        Parse a PQL query string and return its structured dictionary representation.

        The function performs the following steps:
            - creates an ANTLR input stream from the given pql_query string;
            - tokenizes the input using Lexer_PQL;
            - parses the token stream with Parser_PQL to build a parse tree;
            - visits the parse tree using PQLVisitor to produce a dictionary representation.

        Args
        ----
            pql_query : str
                The PQL query string to be parsed.
        
        Returns
        -------
            dict
                A dictionary representing the parsed structure of the PQL query.
        """
        
        input_stream = InputStream(pql_query)
        lexer = Lexer_PQL(input_stream)
        token_stream = CommonTokenStream(lexer)
        
        parser = Parser_PQL(token_stream)
        tree = parser.query()

        query_dict = self.pql_visitor.visit(tree)
        return query_dict 
    

    def build_condition(self, 
                        cond_dict : dict,
                        ptable_name : str, 
                        ppk_name : str) -> str:
        r"""
        Build a SQL query string representing a single conditional expression.

        The function constructs a SQL subquery based on the condition type (CType)
        and condition structure (CondType) defined in cond_dict. 
        It determines whether the condition involves an aggregation, a column reference,
        or a direct value comparison, and generates the appropriate SQL code.

        The resulting query filters rows from the subquery defined by 
        the corresponding CondType and applies the comparison condition.

        Parameters
        ----------
            `cond_dict` : dict
                Dictionary describing the condition.
            `ptable_name` : str
                Name of the parent table used in the condition.
            `ppk_name` : str
                Name of the primary key column for the parent table.

        Returns
        -------
            str
                A SQL query string representing the constructed conditional subquery.
        """

        ctype = cond_dict["CType"]
        cond_type = cond_dict["CondType"]
        
        column_name = "col_for_comp"
        table_query = None
        match cond_type:
            case "aggregation":
                table_query = self.build_aggregation(cond_dict["Aggregation"], ptable_name, ppk_name)
            case "id_dot_id": # STATIC TASK
                table_query = self.build_id_dot_id(cond_dict, ptable_name, ppk_name)
            case _:
                pass
        
        cond = None
        match ctype:
            case "num":
                cond = build_num_condition(cond_dict)
            case "str":
                cond = build_str_condition(cond_dict)
            case "null":
                cond = build_null_condition(cond_dict)
            case _:
                pass
        
        res_query = f"""
                        SELECT 
                            *
                        FROM 
                            ({table_query}) tq
                        WHERE
                            {cond(column_name)}"""
        
        return res_query
    

    def build_id_dot_id(self,
                        some_dict : dict,
                        ptable_name : str,
                        ppk_name : str) -> str:
        table_name = some_dict["Table"]
        # TODO column can be "*" DONE
        column_name = some_dict["Column"]

        fk = self.find_fk(table_name, ptable_name, ppk_name)

        res_query = f"""
                        SELECT 
                            {fk}          AS fk,
                            {column_name} AS col_for_comp
                        FROM
                            {table_name}"""

        return res_query


    def find_fk(self, 
                ctable_name : str, 
                ptable_name : str,
                ppk_name : str) -> str:
        r"""
        Find the foreign key column in a child table that references the parent table.

        The function searches for the column in the child table (`ctable_name`)
        that serves as a foreign key referencing the primary key of the parent table (`ptable_name`).
        If the child and parent tables are the same, the function returns the primary key name.

        Args
        ----
            `ctable_name` : str
                Name of the child table.
            `ptable_name` : str
                Name of the parent table.
            `ppk_name` : str
                Name of the primary key column in the parent table.

        Returns
        -------
            str
                The name of the foreign key column in the child table that references the parent table.
                Returns an empty string if no foreign key relationship is found.
        """

        if ctable_name == ptable_name:
            return ppk_name
        
        ctable = self.db.table_dict[ctable_name]
        for k, v in ctable.fkey_col_to_pkey_table.items():
            if v == ptable_name:
                return k
        
        return ""


    def build_where(self, 
                    query_dict : dict,
                    ptable_name : str,  
                    ppk_name : str) -> str:
        expr_dict = query_dict["Expr"]
        expr_query = self.build_expr(expr_dict, ptable_name, ppk_name)
        return expr_query
    
    

        