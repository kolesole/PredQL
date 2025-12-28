"""Helper utilities for PredQL showcase notebooks."""

from antlr4 import CommonTokenStream, InputStream, TerminalNode
from relbench.base import Database

from predql.converter import ConverterPredQL, SConverterPredQL, TConverterPredQL
from predql.parser import LexerPredQL, ParserPredQL
from predql.visitor import VisitorPredQL


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
    lexer = LexerPredQL(input_stream)
    token_stream = CommonTokenStream(lexer)
    parser = ParserPredQL(token_stream)

    tree = parser.query()

    print("=== Input Query ===")
    print(query)
    print("=== Parse Tree ===")
    print_tree(tree, parser)
    visitor = VisitorPredQL()
    print(visitor.visit(tree))
    print("==================")

    return tree

class ConverterShowcaseHelper:
    predql_converter: ConverterPredQL

    def __init__(self, db: Database, timestamps=None):

        if timestamps is not None:
            self.predql_converter = TConverterPredQL(db, timestamps)
        else:
            self.predql_converter = SConverterPredQL(db)

    def convert_query(self, query):
        print("========================================")
        print(query)
        table = self.predql_converter.convert(query)
        print(table)
        print("========================================")

