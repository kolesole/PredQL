import sys
import os

BASE_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
sys.path.insert(0, BASE_DIR)

from antlr4 import *
from antlr4_parser.Lexer_PQL import Lexer_PQL
from antlr4_parser.Parser_PQL import Parser_PQL
from pql_visitor.PQLVisitor import PQLVisitor
from pql_converter.Converter import PQLConverter

def print_tree(node, parser, indent=0):
   
    space = '  '

    if isinstance(node, TerminalNode):
        print(f"{space}Terminal: {node.getText()} ({parser.symbolicNames[node.getSymbol().type]})")
    else:
        rule_name = parser.ruleNames[node.getRuleIndex()]
        print(f"{space}Rule: {rule_name}")
        for child in node.getChildren():
            print_tree(child, parser, indent + 1)

def parse_query(query: str):
    input_stream = InputStream(query)
    lexer = Lexer_PQL(input_stream)
    token_stream = CommonTokenStream(lexer)
    parser = Parser_PQL(token_stream)

    tree = parser.query()
    
    print("=== Input Query ===")
    print(query)
    print("=== Parse Tree ===")
    print_tree(tree, parser)
    visitor = PQLVisitor()
    print(visitor.visit(tree))
    print("==================")

    return tree

class ConverterShowcaseHelper:
    def __init__(self, dataset):
        self.pql_converter = PQLConverter(dataset.make_db())

    def convert_query(self, query):
        print("========================================")
        print(query)
        table = self.pql_converter.convert(query)
        print(table)
        print("========================================")

