"""Base PredQL converter class."""

import sys
from abc import ABC, abstractmethod

import duckdb
from antlr4 import CommonTokenStream, InputStream

from predql.base import Database, Table
from predql.converter.utils import (
    build_aggr_func,
    build_null_condition,
    build_num_condition,
    build_str_condition,
    get_div_line,
)
from predql.parser import LexerPredQL, ParserPredQL
from predql.validator import ErrorCollector, Validator
from predql.visitor import Visitor


class Converter(ABC):
    r"""Base abstract PredQL converter class for conversion PredQL -> SQL.

    Provides shared functionality for temporal and static PredQL converters.
    Some methods are abstract and must be implemented by concrete subclasses,
    but others provide common logic used in both static and temporal conversion.

    Attributes:
        validator (Validator): Validator instance for semantic validation of parsed queries.
    """

    # validator instance for semantic validation of parsed queries
    # set in concrete subclasses
    validator: Validator

    def __init__(self, db: Database) -> None:
        r"""Base constructor.

        Initializes *`Database`* instance, *`Visitor`* instance, and *`ErrorCollector`* instance
        for storing validation errors.

        Args:
            db (Database): *`Database`* instance containing the schema and data tables to be queried.

        Returns:
            out (None):
        """
        self.conn = None
        self.db = db
        self.visitor = Visitor()
        self.collector = ErrorCollector()

    @abstractmethod
    def convert(self, predql_query: str, execute: bool = False) -> str | Table:
        r"""Abstract conversion method.

        Main entry point.

        Note:
            For explanation of the conversion process, see concrete subclasses.
        """
        pass

    @abstractmethod
    def build_for_each(self, for_each_dict: dict) -> tuple[str, str, str]:
        r"""Abstrac method to build the SQL query for the for each part of the PredQL query.

        Note:
            For explanation of the building process, see concrete subclasses.
        """
        pass

    @abstractmethod
    def build_predict(self, predict_dict: dict, ptable: str, ppk: str, for_each_query: str) -> str:
        r"""Abstract method to build the SQL query for the predict part of the PredQL query.

        Note:
            For explanation of the building process, see concrete subclasses.
        """
        pass

    @abstractmethod
    def build_expr(self, expr_dict: dict, ptable: str, ppk: str) -> str:
        r"""Abstract method to build the SQL query for the expression part of the PredQL query.

        Note:
            For explanation of the building process, see concrete subclasses.
        """
        pass

    @abstractmethod
    def build_aggregation(self, aggr_dict: dict, ptable: str, ppk: str) -> str:
        r"""Abstract method to build the SQL query for the aggregation part of the PredQL query.

        Note:
            For explanation of the building process, see concrete subclasses.
        """
        pass

    def parse_query(self, predql_query: str) -> dict:
        r"""Parses the PredQL query string into a dictionary representation.

        Validates a dictionary representation, prints all errors on stderr
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

    def build_stat_where(self, where_dict: dict, ptable: str, ppk: str) -> str:
        r"""Builds the SQL query for the static WHERE part of the PredQL query.

        Filters a ptable before using.

        Args:
            where_dict (dict): Dictionary representation of the WHERE part of the PredQL query.
            ptable (str): Name of the parent table.
            ppk (str): Name of the primary key column in the parent table.

        Returns:
            where_query (str): SQL query string representing the filtered ptable.
        """
        # create division markers for formatted output
        div_line_expr1 = get_div_line("STAT_WHERE_START")
        div_line_expr2 = get_div_line("STAT_WHERE_END")

        expr_query = self.build_stat_expr(where_dict["Expr"].value, ptable, ppk)
        expr_query = expr_query.replace("\n", "\n" + 4 * " ") + "\n"

        where_query = (
            f"{div_line_expr1}\n"
            "SELECT\n"
            "    *\n"
            "FROM\n"
            f"    {ptable} __UNSORTED_AGGR_TBL__\n"
            f"JOIN\n"
            f"    ({expr_query}) __EXPR__\n"
            "ON\n"
            f"    __UNSORTED_AGGR_TBL__.{ppk} = __EXPR__.fk\n"
            f"{div_line_expr2}"
        )

        return where_query

    def build_stat_expr(self, expr_dict: dict, ptable: str, ppk: str) -> str:
        r"""Builds a SQL query for the static expression part of the PredQL query.

        Args:
            expr_dict (dict): Dictionary representation of the expr part of the PredQL query.
            ptable (str): Name of the parent table.
            ppk (str): Name of the primary key column in the parent table.

        Returns:
            expr_query (str): SQL query string representing the expr part of the PredQL query.
        """
        # create division markers for formatted output
        div_line_expr1 = get_div_line("STAT_EXPR_START")
        div_line_expr2 = get_div_line("STAT_EXPR_END")

        # if expression is composite (AND/OR) -> recursively build left and right sub-expressions
        # otherwise -> build single condition expression
        if isinstance(expr_dict, dict) and "Op" in expr_dict:
            # build left expession
            left_expr = self.build_stat_expr(expr_dict["LeftExpr"], ptable, ppk)
            left_expr = left_expr.replace("\n", "\n" + 4 * " ") + "\n"
            # build right expression
            right_expr = self.build_stat_expr(expr_dict["RightExpr"], ptable, ppk)
            right_expr = right_expr.replace("\n", "\n" + 4 * " ") + "\n"

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
                f"    ({left_expr}) __LEFT_EXPR__\n"
                f"{filt}\n"
                "SELECT\n"
                "    fk,\n"
                f"FROM ({right_expr}) __RIGHT_EXPR__\n"
                f"{div_line_expr2}"
            )
        else:
            expr_query = self.build_condition(expr_dict.value, ptable, ppk, stat=True)

        return expr_query

    def build_condition(self, cond_dict: dict, ptable: str, ppk: str, stat: bool = False) -> str:
        r"""Builds a SQL query for a condition part of the PredQL query.

        Args:
            cond_dict (dict): Dictionary representation of the condition part of the PredQL query.
            ptable (str): Name of the parent table.
            ppk (str): Name of the primary key column in the parent table.
            stat (bool): Flag indicating whether the condition is part of a static expression or not.

        Returns:
            res_query (str): SQL query string representing the condition part of the PredQL query.
        """
        # check condition type and build main query for condition accordingly
        # aggregation / id_dot_id
        cond_type = cond_dict["CondType"]
        match cond_type:
            case "aggregation":
                if stat:
                    main_query = self.build_stat_aggregation(cond_dict["Aggregation"].value, ptable, ppk)
                else:
                    main_query = self.build_aggregation(cond_dict["Aggregation"].value, ptable, ppk)
            case "id_dot_id":
                main_query = self.build_id_dot_id(cond_dict, ptable, ppk)
            case _:
                pass
        main_query = main_query.replace("\n", "\n" + 4 * " ") + "\n"

        # column to compare in condition
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

        # handle NOT operator
        not_op = "NOT " if cond_dict["NOT"] else ""

        # create division markers for formatted output
        div_line1 = get_div_line("CONDITION_START")
        div_line2 = get_div_line("CONDITION_END")

        # build final condition query
        res_query = (
            f"{div_line1}\nSELECT\n    *\nFROM\n    ({main_query})\nWHERE\n    {not_op}{cond(comp_col)}\n{div_line2}"
        )

        return res_query

    def build_stat_aggregation(self, aggr_dict: dict, ptable: str, ppk: str) -> str:
        r"""Builds a SQL query for a static PredQL aggregation.

        Args:
            aggr_dict (dict): Parsed aggregation dictionary containing 'Table', 'Column', 'Where'(optional) keys.
            ptable (str): Name of the parent table.
            ppk (str): Name of the primary key column in the parent table.

        Returns:
            aggr_query (str): SQL query returning pairs (fk, comp_col).
        """
        # extract aggregation table
        aggr_table = aggr_dict["Table"].value

        # find foreign key column in the aggregation table that links to parent table
        fk = self._find_fk(aggr_table, ptable, ppk)

        # build SQL aggregation function with proper column references
        aggr_dict["Column"].value = self._find_column(aggr_table, aggr_dict["Column"].value)
        aggr_func = build_aggr_func(aggr_dict)
        aggr = aggr_func("__AGGR_TBL__").replace("\n", "\n" + 4 * " ") + "\n"

        # build static WHERE query if exists
        if where := aggr_dict["Where"]:
            aggr_ppk = self._find_pkey(aggr_table)
            aggr_table = self.build_stat_where(where.value, aggr_table, aggr_ppk)
            aggr_table = f"({aggr_table})"

        # create division markers for formatted output
        div_line_aggr1 = get_div_line("STAT_AGGREGATION_START")
        div_line_aggr2 = get_div_line("STAT_AGGREGATION_END")

        # build aggregation query
        aggr_query = (
            f"{div_line_aggr1}\n"
            "SELECT\n"
            f"    __PARENT__.{ppk} AS fk,\n"
            f"    {aggr} AS comp_col,\n"
            "FROM\n"
            f"    {ptable} __PARENT__\n"
            "LEFT JOIN\n"
            f"    {aggr_table} __AGGR_TBL__\n"
            "ON\n"
            f"    __AGGR_TBL__.{fk} = __PARENT__.{ppk}\n"
            "GROUP BY\n"
            f"    __PARENT__.{ppk}\n"
            f"{div_line_aggr2}"
        )

        return aggr_query

    def build_id_dot_id(self, some_dict: dict, ptable: str, ppk: str) -> str:
        r"""Builds the SQL query for a table.column(id_dot_id) part of the PredQL query.

        Args:
            some_dict (dict): Dictionary containing 'Table', 'Column' keys.
            ptable (str): Name of the parent table.
            ppk (str): Name of the primary key column in the parent table.

        Returns:
            res_query (str): SQL query string representing the id_dot_id part of the PredQL query.
        """
        table = some_dict["Table"].value
        column = self._find_column(table, some_dict["Column"].value)

        # column to compare in condition
        comp_col = "comp_col"
        # find foreign key column in child table referencing parent table
        fk = self._find_fk(table, ptable, ppk)

        # create division markers for formatted output
        div_line1 = get_div_line("ID_DOT_ID_START")
        div_line2 = get_div_line("ID_DOT_ID_END")

        # if foreign key exists -> build simple query on the child table
        # otherwise -> try to find foreign key in the opposite direction and build left join query
        if fk := self._find_fk(table, ptable, ppk):
            res_query = (
                f"{div_line1}\nSELECT\n    {fk} AS fk,\n    {column} AS {comp_col}\nFROM\n    {table}\n{div_line2}"
            )
        elif fk := self._find_fk(ptable, table, ppk=None):
            res_query = (
                f"{div_line1}\n"
                "SELECT\n"
                f"    __PT__.{ppk} AS fk,\n"
                f"    __T__.{column} AS {comp_col}\n"
                "FROM\n"
                f"    {ptable} __PT__\n"
                "LEFT JOIN\n"
                f"    {table} __T__\n"
                "ON\n"
                f"    __PT__.{fk} = __T__.{self._find_pkey(table)}\n"
                f"{div_line2}"
            )

        return res_query

    ################## Helper methods ##################

    def _register_db(self) -> None:
        """Registers all tables from the *`Database`* instance in the *`DuckDB`* connection.

        Returns:
            out (None):
        """
        if self.conn:
            return

        self.conn = duckdb.connect()

        for name, table in self.db.table_dict.items():
            self.conn.register(name, table.df)

    def _find_table(self, table: str) -> tuple[str, Table] | None:
        r"""Finds a *`Table`* object in the *`Database`* by its name (case-insensitive).

        Args:
            table (str): Name of the table to find.

        Returns:
            out (tuple[str, Table] | None): Tuple of the form (original_table_name, Table)
                Returns None if no table with the given name was found.
        """
        # k ... name of the table
        # v ... Table object
        for k, v in self.db.table_dict.items():
            if k.lower() == table.lower():
                return k, v

        return None

    def _find_column(self, table: str, column: str) -> str | None:
        r"""Finds a column name in a table (case-insensitive).

        Args:
            table (str): Name of the table.
            column (str): Name of the column to find.

        Returns:
            out (str | None): Original name of the column if found, None otherwise.
        """
        _, table_obj = self._find_table(table)
        if table_obj:
            # if column is "*" -> return primary key column
            if column == "*":
                return table_obj.pkey_col
            for col in table_obj.df.columns:
                if col.lower() == column.lower():
                    return col
        return None

    def _find_ptable(self, table: str, fk: str) -> str | None:
        r"""Finds the parent table name that a given table references through a given foreign key (case-insensitive).

        Args:
            table (str): Name of the child table.
            fk (str): Name of the foreign key column in the child table.

        Returns:
            out (str | None): Name of the parent table that the child table references through the foreign key column
                if found, None otherwise.
        """
        _, table_obj = self._find_table(table)

        # k ... name of foreign key column in child table
        # v ... name of referenced parent table
        for k, v in table_obj.fkey_col_to_pkey_table.items():
            if k.lower() == fk.lower():
                return v

        return None

    def _find_fk(self, ctable: str, ptable: str, ppk: str) -> str | None:
        r"""Finds the foreign key column in a child table that references the parent table (case-insensitive).

        Args:
            ctable (str): Name of the child table.
            ptable (str): Name of the parent table.
            ppk (str): Name of the primary key column in the parent table.

        Returns:
            out (str | None): Name of the foreign key column in the child table if found, None otherwise.
        """
        # if child and parent table are the same -> return primary key
        if ctable.lower() == ptable.lower():
            return ppk

        _, ctable_obj = self._find_table(ctable)

        # k ... name of foreign key column in child table
        # v ... name of referenced parent table
        for k, v in ctable_obj.fkey_col_to_pkey_table.items():
            if v.lower() == ptable.lower():
                return k

        return None

    def _find_pkey(self, table: str) -> str | None:
        r"""Finds the primary key column of a table (case-insensitive).

        Args:
            table (str): Name of the table.

        Returns:
            out (str | None): Name of the primary key column of the table if found, None otherwise.
        """
        _, table_obj = self._find_table(table)
        return table_obj.pkey_col
