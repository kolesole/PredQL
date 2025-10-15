import sys
import os

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from antlr4 import *
from Lexer_PQL import Lexer_PQL
from Parser_PQL import Parser_PQL
from PQLVisitor import PQLVisitor

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

    print("=== Parse Tree ===")
    print_tree(tree, parser)
    visitor = PQLVisitor()
    print(visitor.visit(tree))
    print("==================")

    return tree

if __name__ == "__main__":
    with open('showcase.txt', "r") as f:
        for l in f:
            query = l.strip()
            print(query)
            parse_query(query)
    # while 1:
    #     # query = input("Enter PQL-query: ")
    #     parse_query(query)

