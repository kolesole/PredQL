from predql.base.table import Table

class Database:
    
    def __init__(self,
                 table_dict : dict[str, Table]) -> None:
        self.table_dict = table_dict
    
    
    def __repr__(self) -> str:
        return "================= Database ================\n" + "".join(
            f"Table Name: {name}\n{table}\n"
            for name, table in self.table_dict.items()
        )
    
    # def __contains__(self,
    #                  table_name : str) -> bool:
    #     return table_name in self.table_dict
    
    # def __getitem__(self, 
    #                 table_name : str) -> Table:
    #     return self.table_dict.get(table_name)
    
    # def __setitem__(self, 
    #                 table_name : str, 
    #                 table      : Table) -> None:
    #     self.table_dict[table_name] = table
    
    # def __delitem__(self, 
    #                 table_name : str) -> None:
    #     if table_name in self.table_dict:
    #         del self.table_dict[table_name]
    