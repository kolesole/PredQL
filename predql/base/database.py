"""Database class to hold multiple tables."""

from functools import cached_property

import pandas as pd

from predql.base.table import Table


class Database:
    r"""Represents a database containing multiple related tables.

    The *`Database`* class stores a collection of *`Table`* objects and provides
    a representation method for displaying all tables in the database.
    """

    def __init__(self, table_dict: dict[str, Table]) -> None:
        r"""Initializes *`Database`* with a dictionary of tables.

        Args:
            table_dict (dict[str, Table]): Dictionary where keys are table
            names and values are Table objects.

        Returns:
            out (None):
        """
        self.table_dict = table_dict

    def __repr__(self) -> str:
        r"""Returns a string representation of the database.

        Returns:
            out (str): Formatted string showing all tables in the database.
        """
        return "================= Database ================\n" + "".join(
            f"Table Name: {name}\n{table}\n" for name, table in self.table_dict.items()
        )

    @cached_property
    def min_timestamp(self) -> pd.Timestamp | None:
        r"""Returns the minimum timestamp across all tables in the database, if any time columns exist.

        Returns:
            min_timestamp (pd.Timestamp | None): Minimum timestamp across all tables, or None if no time columns.
        """
        min_timestamps = [table.min_timestamp for table in self.table_dict.values() if table.time_col]
        return min(min_timestamps) if min_timestamps else None

    @cached_property
    def max_timestamp(self) -> pd.Timestamp | None:
        r"""Returns the maximum timestamp across all tables in the database, if any time columns exist.

        Returns:
            max_timestamp (pd.Timestamp | None): Maximum timestamp across all tables, or None if no time columns.
        """
        max_timestamps = [table.max_timestamp for table in self.table_dict.values() if table.time_col]
        return max(max_timestamps) if max_timestamps else None
