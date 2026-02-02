"""Base PredQL converter module."""

from abc import abstractmethod
from antlr4 import CommonTokenStream, InputStream
import duckdb
import sys

from predql.base import Database, Table
from predql.converter.utils import (
    build_null_condition,
    build_num_condition,
    build_str_condition,
    get_div_line
)
from predql.parser.gen.LexerPredQL import LexerPredQL
from predql.parser.gen.ParserPredQL import ParserPredQL
from predql.validator import ErrorCollector
from predql.visitor import Visitor


class Converter:
    r"""Base PredQL converter class for conversion PredQL -> SQL.

    Provides shared functionality for temporal and static PredQL converters.\
    Some methods are astract and must be implemented by concrete subclasses,\
    but others provide common logic used in both static and temporal conversion.
    """

    tmp : bool

    def __init__(self,
                 db: Database) -> None:
        r"""Base constructor.

        Initializes *`Database`* instance, *`DuckDB`* connection, *`VisitorPredQL`* instance and\
        registers all database tables in *`DuckDB`* connection.

        Args:
            db (Database): *`Database`* instance containing the schema and data tables to be queried.

        Returns:
            out (None):
        """
        self.db = db
        self.predql_visitor = Visitor()
        self.conn = duckdb.connect()
        # register all tables in DuckDB connection
        for name, table in db.table_dict.items():
            self.conn.register(name, table.df)


    @abstractmethod
    def convert(self,
                predql_query : str) -> Table:
        r"""Abstract conversion method.

        Main entry point.

        Note:
            For explanation of the conversion process, see concrete subclasses.
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
        r"""Parses the PredQL query string into a dictionary representation.

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
        collector = ErrorCollector()
        parser.addErrorListener(collector)
        tree = parser.query()

        query_dict = self.predql_visitor.visit(tree)

        if len(collector) > 0:
            print(collector, file=sys.stderr)
            sys.exit(1)

        return query_dict


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
                main_query = self.build_aggregation(cond_dict["Aggregation"], ptable, ppk)
            case "id_dot_id":
                main_query = self.build_id_dot_id(cond_dict, ptable, ppk)
            case _:
                raise ValueError(f"Unknown condition type: {cond_type}")
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
                raise ValueError(f"Unknown condition ctype: {ctype}")

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
