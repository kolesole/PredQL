#!/bin/bash
# Regenerate ANTLR parser files from grammar
# Usage: ./regenerate_parser.sh

# Activate venv
source .venv/bin/activate

# Navigate to grammar directory
cd predql/parser

mkdir -p gen

# Regenerate parser files using Python module directly
python3 -c "
from antlr4_tool_runner import tool; 
import sys; 
sys.argv = [
    'antlr4', 
    '-Dlanguage=Python3', 
    '-visitor', 
    '-o', 'gen',
    'ParserPredQL.g4', 
    'LexerPredQL.g4'
]; 
tool()
"

echo "Parser files regenerated successfully!"

