from relbench.base import Database

from antlr4 import TerminalNode, InputStream, CommonTokenStream

from pql.parser import LexerPQL, ParserPQL
from pql.visitor import VisitorPQL
from pql.converter import ConverterPQL, SConverterPQL, TConverterPQL 

def print_tree(node, parser):
   
    space = '  '

    if isinstance(node, TerminalNode):
        print(f"{space}Terminal: {node.getText()} ({parser.symbolicNames[node.getSymbol().type]})")
    else:
        rule_name = parser.ruleNames[node.getRuleIndex()]
        print(f"{space}Rule: {rule_name}")
        for child in node.getChildren():
            print_tree(child, parser)

def parse_query(query: str):
    input_stream = InputStream(query)
    lexer = LexerPQL(input_stream)
    token_stream = CommonTokenStream(lexer)
    parser = ParserPQL(token_stream)

    tree = parser.query()
    
    print("=== Input Query ===")
    print(query)
    print("=== Parse Tree ===")
    print_tree(tree, parser)
    visitor = VisitorPQL()
    print(visitor.visit(tree))
    print("==================")

    return tree

class ConverterShowcaseHelper:
    pql_converter: ConverterPQL
    
    def __init__(self, db: Database, timestamps=None):
        
        if timestamps is not None:
            self.pql_converter = TConverterPQL(db, timestamps)
        else:
            self.pql_converter = SConverterPQL(db)

    def convert_query(self, query):
        print("========================================")
        print(query)
        table = self.pql_converter.convert(query)
        print(table)
        print("========================================")

