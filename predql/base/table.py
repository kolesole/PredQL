"""Table class representing a database table with metadata."""

import pandas as pd

class Table:
    r"""Represents a database table with its data and relational metadata.

    The *`Table`* class encapsulates a pandas DataFrame along with metadata about  
    primary keys, foreign keys, and temporal columns. 
    """
    
    def __init__(self,
                 df                     : pd.DataFrame,
                 fkey_col_to_pkey_table : dict[str, str]=None,
                 pkey_col               : str=None,
                 time_col               : str=None) -> None:
        r"""Initializes *`Table`* with data and metadata.
        
        Args:
            df (pd.DataFrame): The table data.
            fkey_col_to_pkey_table (dict, optional): Dictionary mapping foreign key column names to parent table names.  
                    Default = None.
            pkey_col (str, optional): Primary key column name.  
                    Default = None.
            time_col (str, optional): Timestamp column name for temporal tables.  
                    Default = None.
        """
        self.df = df
        self.fkey_col_to_pkey_table = fkey_col_to_pkey_table
        self.pkey_col = pkey_col
        self.time_col = time_col
    
    
    def __repr__(self) -> str:
        r"""Returns a string representation of the table.
        
        Returns:
            out (str): Formatted string showing *`DataFrame`* and all metadata.
        """
        return (
            "------------------ Table ------------------\n"
            f"DataFrame:\n{self.df}\n"
            f"Foreign Key Columns to Primary Key Tables: {self.fkey_col_to_pkey_table}\n"
            f"Primary Key Column: {self.pkey_col}\n"
            f"Time Column: {self.time_col}\n"
            "-------------------------------------------"
        )
    