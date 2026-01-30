import pandas as pd

class Table:
    
    def __init__(self,
                 df                     : pd.DataFrame,
                 fkey_col_to_pkey_table : dict=None,
                 pkey_col               : str=None,
                 time_col               : str=None) -> None:
        
        self.df = df
        self.fkey_col_to_pkey_table = fkey_col_to_pkey_table
        self.pkey_col = pkey_col
        self.time_col = time_col
    
    def __repr__(self) -> str:
        return (
            "------------------ Table ------------------\n"
            f"DataFrame:\n{self.df}\n"
            f"Foreign Key Columns to Primary Key Tables: {self.fkey_col_to_pkey_table}\n"
            f"Primary Key Column: {self.pkey_col}\n"
            f"Time Column: {self.time_col}\n"
            "-------------------------------------------"
        )
    