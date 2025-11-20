#!/bin/bash
# Regenerate ANTLR parser files from grammar
# Usage: ./regenerate_parser.sh

# Activate venv
source .venv/bin/activate

# Navigate to grammar directory
cd grammar/antlr4_parser

# Regenerate parser files using Python module directly
python -c "from antlr4_tool_runner import tool; import sys; sys.argv = ['antlr4', '-Dlanguage=Python3', '-visitor', 'Parser_PQL.g4', 'Lexer_PQL.g4']; tool()"

echo "Parser files regenerated successfully!"

