"""Database class to hold multiple tables."""

from predql.base.table import Table

class Database:
    r"""Represents a database containing multiple related tables.
    
    The *`Database`* class stores a collection of *`Table`* objects and provides  
    a representation method for displaying all tables in the database.
    """
    
    def __init__(self,
                 table_dict : dict[str, Table]) -> None:
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
            f"Table Name: {name}\n{table}\n"
            for name, table in self.table_dict.items()
        )
    