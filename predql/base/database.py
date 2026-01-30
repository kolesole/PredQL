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
    