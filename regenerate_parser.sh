#!/bin/bash
# Regenerate ANTLR parser files from grammar
# Usage: ./regenerate_parser.sh

# Activate venv
source .venv/bin/activate

# Navigate to grammar directory
cd pql/parser

mkdir -p gen

# Regenerate parser files using Python module directly
python -c "
from antlr4_tool_runner import tool; 
import sys; 
sys.argv = [
    'antlr4', 
    '-Dlanguage=Python3', 
    '-visitor', 
    '-o', 'gen',
    'ParserPQL.g4', 
    'LexerPQL.g4'
]; 
tool()
"

echo "Parser files regenerated successfully!"

