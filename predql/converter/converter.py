"""Base PredQL converter class."""

from abc import ABC, abstractmethod
from antlr4 import CommonTokenStream, InputStream
import duckdb
import sys

from predql.base import Database, Table
from predql.parser import LexerPredQL, ParserPredQL
from predql.validator import ErrorCollector, Validator
from predql.visitor import Visitor

from predql.converter.utils import (
    build_null_condition,
    build_num_condition,
    build_str_condition,
    get_div_line
)


class Converter(ABC):
    r"""Base abstract PredQL converter class for conversion PredQL -> SQL.

    Provides shared functionality for temporal and static PredQL converters.  
    Some methods are abstract and must be implemented by concrete subclasses,  
    but others provide common logic used in both static and temporal conversion.
    """

    # validator instance for semantic validation of parsed queries 
    # set in concrete subclasses
    validator : Validator

    def __init__(self,
                 db: Database) -> None:
        r"""Base constructor.

        Initializes *`Database`* instance, *`DuckDB`* connection, *`Visitor`* instance,  
        registers all database tables in *`DuckDB`* connection and initializes *`ErrorCollector`*  
        for storing validation errors.

        Args:
            db (Database): *`Database`* instance containing the schema and data tables to be queried.

        Returns:
            out (None):
        """
        self.db = db
        self.visitor = Visitor()
        self.conn = duckdb.connect()
        # register all tables in DuckDB connection
        for name, table in db.table_dict.items():
            self.conn.register(name, table.df)
        self.collector = ErrorCollector()


    @abstractmethod
    def convert(self,
                predql_query : str,
                show         : bool=False) -> Table:
        r"""Abstract conversion method.

        Main entry point.

        Note:
            For explanation of the conversion process, see concrete subclasses.
        """
        pass


    @abstractmethod
    def build_for_each(self,
                       for_each_dict : dict) -> tuple[str, str, str]:
        r""""Abstrac method to build the SQL query for the for each part of the PredQL query.
        
        Note:
            For explanation of the building process, see concrete subclasses.
        """
        pass
    

    @abstractmethod
    def build_predict(self,
                      predict_dict   : dict,
                      ptable         : str,
                      ppk            : str,
                      for_each_query : str) -> str:
        r"""Abstract method to build the SQL query for the predict part of the PredQL query.

        Note:
            For explanation of the building process, see concrete subclasses.
        """
        pass


    @abstractmethod
    def build_expr(self,
                   expr_dict : dict,
                   ptable    : str,
                   ppk       : str) -> str:
        r"""Abstract method to build the SQL query for the expression part of the PredQL query.

        Note:
            For explanation of the building process, see concrete subclasses.
        """
        pass

    
    @abstractmethod
    def build_aggregation(self,
                          aggr_dict : dict,
                          ptable    : str,
                          ppk       : str) -> str:
        r"""Abstract method to build the SQL query for the aggregation part of the PredQL query.

        Note:
            For explanation of the building process, see concrete subclasses.
        """
        pass


    def parse_query(self,
                    predql_query : str) -> dict:
        r"""Parses the PredQL query string into a dictionary representation,  
        validates a dictionary representation, prints all errors on stderr  
        and exit the program if any errors were found.

        Args:
            predql_query (str): The PredQL query string to be parsed.

        Returns:
            query_dict (dict): Dictionary representation of the parsed PredQL query.
        """
        input_stream = InputStream(predql_query)
        lexer = LexerPredQL(input_stream)
        token_stream = CommonTokenStream(lexer)

        parser = ParserPredQL(token_stream)
        parser.removeErrorListeners()
        parser.addErrorListener(self.collector)
        tree = parser.query()

        query_dict = self.visitor.visit(tree)
        
        if self.validator:
            self.validator.validate(query_dict)

        if len(self.collector) > 0:
            print(self.collector, file=sys.stderr)
            self.collector.clear()
            sys.exit(1)

        return query_dict
    
    ####################################################################################
    # NOTE: FOR NOW WORKS ONLY WITH ID_DOT_ID OR EXPRS WITH ID_DOT_ID
    # NOT WITH AGGREGATION
    def build_stat_where(self,
                         where_dict : dict,
                         ptable     : str,
                         ppk        : str) -> str:
        expr_query = self.build_stat_expr(where_dict["Expr"].value, ptable, ppk)
        where_query = (
             "SELECT\n"
             "    *\n"
             "FROM\n"
            f"    {ptable} unsorted_aggr_tbl\n"
            f"JOIN\n"
            f"    ({expr_query}\n) expr\n"
             "ON\n"
            f"    unsorted_aggr_tbl.{ppk} = expr.fk\n" 
        )

        return where_query
    

    def build_stat_expr(self,
                        expr_dict : dict,
                        ptable    : str,
                        ppk       : str) -> str:
        # create division markers for formatted output
        div_line_expr1 = get_div_line("EXPR_START")
        div_line_expr2 = get_div_line("EXPR_END")

        # if expression is composite (AND/OR) -> recursively build left and right sub-expressions
        # otherwise -> build single condition expression
        if isinstance(expr_dict, dict) and "Op" in expr_dict:
            # build left expession
            left_expr = self.build_stat_expr(expr_dict["LeftExpr"], ptable, ppk)
            left_expr = left_expr.replace("\n", "\n" + 4*" ") + "\n"
            # build right expression
            right_expr = self.build_stat_expr(expr_dict["RightExpr"], ptable, ppk)
            right_expr = right_expr.replace("\n", "\n" + 4*" ") + "\n"

            # check operation and convert to SQL format for tables
            op = expr_dict["Op"].value.lower()
            if op == "and":
                filt = "INTERSECT"
            elif op == "or":
                filt = "UNION"
            else:
                pass

            expr_query = (
                f"{div_line_expr1}\n"
                 "SELECT\n"
                 "    fk,\n"
                 "FROM\n"
                f"    ({left_expr}) left_expr\n"
                f"{filt}\n"
                 "SELECT\n"
                 "    fk,\n"
                f"FROM ({right_expr}) right_expr\n"
                f"{div_line_expr2}"
            )
        else:
            expr_query = self.build_condition(expr_dict.value, ptable, ppk)

        return expr_query
    
    #######################################################################################

    def build_condition(self,
                        cond_dict : dict,
                        ptable    : str,
                        ppk       : str) -> str:
        r"""Builds the SQL query for a condition part of the PredQL query.

        Args:
            cond_dict (dict): Dictionary representation of the condition part of the PredQL query.
            ptable (str): Name of the parent table.
            ppk (str): Name of the primary key column in the parent table.

        Returns:
            res_query (str): SQL query string representing the condition part of the PredQL query.
        """
        # check condition type and build main query for condition accordingly
        # aggregation / id_dot_id
        cond_type = cond_dict["CondType"]
        match cond_type:
            case "aggregation":
                main_query = self.build_aggregation(cond_dict["Aggregation"].value, ptable, ppk)
            case "id_dot_id":
                main_query = self.build_id_dot_id(cond_dict, ptable, ppk)
            case _:
                pass
        main_query = main_query.replace("\n", "\n" + 4*" ") + "\n"

        # column to compare in condition
        # check build_aggregation and build_id_dot_id
        comp_col = "comp_col"

        # check value condition type and build condition accordingly
        # num / str / null
        ctype = cond_dict["CType"]
        match ctype:
            case "num":
                cond = build_num_condition(cond_dict)
            case "str":
                cond = build_str_condition(cond_dict)
            case "null":
                cond = build_null_condition(cond_dict)
            case _:
                pass

        # create division markers for formatted output
        div_line1 = get_div_line("CONDITION_START")
        div_line2 = get_div_line("CONDITION_END")

        # handle NOT operator
        NOT = "NOT " if cond_dict["NOT"] else ""

        # build final condition query
        res_query = (
            f"{div_line1}\n"
             "SELECT\n"
             "    *\n"
             "FROM\n"
            f"    ({main_query})\n"
             "WHERE\n"
            f"    {NOT}{cond(comp_col)}\n"
            f"{div_line2}"
        )

        return res_query


    def build_id_dot_id(self,
                        some_dict : dict,
                        ptable    : str,
                        ppk       : str) -> str:
        r"""Builds the SQL query for a table.column(id_dot_id) part of the PredQL query.

        Args:
            some_dict (dict): Dictionary containing 'Table', 'Column' keys.
            ptable (str): Name of the parent table.
            ppk (str): Name of the primary key column in the parent table.

        Returns:
            res_query (str): SQL query string representing the id_dot_id part of the PredQL query.
        """
        table = some_dict["Table"].value
        column = some_dict["Column"].value

        # create division markers for formatted output
        div_line1 = get_div_line("ID_DOT_ID_START")
        div_line2 = get_div_line("ID_DOT_ID_END")

        # column to compare in condition
        comp_col = "comp_col"
        # find foreign key column in child table referencing parent table
        fk = self.find_fk(table, ptable, ppk)

        # build final id_dot_id query
        res_query = (
            f"{div_line1}\n"
             "SELECT\n"
            f"    {fk} AS fk,\n"
            f"    {column} AS {comp_col}\n"
             "FROM\n"
            f"    {table}\n"
            f"{div_line2}"
        )

        return res_query


    def find_fk(self,
                ctable : str,
                ptable : str,
                ppk    : str) -> str:
        r"""Finds the foreign key column in a child table that references the parent table.

        Args:
            ctable (str): Name of the child table.
            ptable (str): Name of the parent table.
            ppk (str): Name of the primary key column in the parent table.

        Returns:
            out (str): Name of the foreign key column in the child table.
        """
        # if child and parent table are the same -> return primary key
        if ctable == ptable:
            return ppk

        ctable_dict = self.db.table_dict[ctable]
        # k ... name of foreign key column in child table
        # v ... name of referenced parent table
        for k, v in ctable_dict.fkey_col_to_pkey_table.items():
            if v == ptable:
                return k

        return ""
