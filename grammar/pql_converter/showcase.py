from Converter import PQLConverter
from relbench.datasets.f1 import F1Dataset

f1_dataset = F1Dataset()
pql_converter = PQLConverter(f1_dataset.make_db())

with open('showcase.txt', "r") as f:
    query = ""
    for l in f:
        query += l
        if ';' in l:
            print("========================================")
            print(query)
            table = pql_converter.convert(query)
            print(table)
            print("========================================")
            query = ""
