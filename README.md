# PredQL 

**PredQL** (Predictive Query Language) is a Python framework designed to simplify working with databases in the context of **Relational Deep Learning (RDL)**.

It enables writing shorter, more expressive queries by abstracting away the complexity of temporal joins and sophisticated aggregations.

## 🧠 Features

- 🎯 **ANTLR-based Parser** - Lexer and parser for PredQL syntax
- 🌳 **Parse Tree Visitor** - Transforms PredQL queries into structured dictionaries
- 🔀 **Dual Converters** - Static and temporal SQL conversion
  - 📌 `SConverterPredQL` - Non-temporal predictions
  - ⏰ `TConverterPredQL` - Time-window based temporal predictions with automatic time bucketing
- ⚙️ **Automatic Execution** - Executes generated SQL and returns results as ready-to-use table objects

## ⚙️ Installation

Install PredQL via pip:

```bash
pip install predql
```

## 🚀 Quickstart

### 📌 Static Query

#### 🌪️ Query design

```sql
PREDICT <target_table>.<target_column>
FOR EACH <entity_table>.<primary_key>
[WHERE <condition>|<nested_condition>] 
```

#### 🗒️ NOTES

- All tables which are used must contain `<foreign_key>` which is connected with `<primary_key>` of `<entity_table>`

- `<condition>` design: 

    ```sql
    <table>.<column> <num_condition>|<str_condition>|<null_condition>
    ```
    | Category    | Operators | Right side |
    | :---        | :---      | :--- |
    | **Numeric** | `!=`, `<`, `<=`, `==`, `>`, `>=` | NUMBER
    | **String** | `CONTAINS`, `NOT CONTAINS`, `LIKE`, `NOT LIKE`, `STARTS WITH`, `ENDS WITH`, `=` | STRING
    | **Nullability** | `IS NULL`, `IS NOT NULL` | |

#### 💡 Example 

Predicting student favorite subject:

```python
from predql.converter import SConverterPredQL
from relbench.base import Database

# load your database with tables
db = Database(...)

# create converter
converter = SConverterPredQL(db)

# convert and execute PredQL query
result_table = converter.convert("""
    PREDICT studentInf.favSubject
    FOR EACH students.studentId;
""")

df = result.df() # get dataframe object
```

### ⏰ Temporal Query

#### 🌪️ Query design

```sql
PREDICT <aggregation>
FOR EACH <entity_table>.<primary_key>
[ASSUMING <condition>|<nested_condition>]
[WHERE <condition>|<nested_condition>] 
```

#### 🗒️ NOTES

- All tables which are used must contain `<foreign_key>` which is connected with `<primary_key>` of `<entity_table>`

- `<condition>` the same as in static 

- `<aggregation>` design:

    ```sql
    <aggr_func>(<target_table>.<target_column>[, <start>, <end>, <measure_unit>] [WHERE <condition>|<nested_condition>])
    ```

- Available aggregation functions:

    | Function | Description
    | :--- | :--- |
    | `AVG` | Average value 
    | `MAX` | Maximum value 
    | `MIN` | Minimum value 
    | `SUM` | Sum of values 
    | `COUNT` | Count of non-null values
    | `COUNT_DISTINCT` | Count of distinct values
    | `FIRST` | First value (ordered by time)
    | `LAST` | Last value (ordered by time) 
    | `LIST_DISTINCT` | List of distinct values ordered by count

- Time window parameters:
  - `<start>` - Start offset must be `≤ 0` for `<ASSUMING>` and `≥ 0` for `<PREDICT>|<WHERE>`
  - `<end>` - End offset must be `≤ 0` for `<ASSUMING>` and `≥ 0` for `<PREDICT>|<WHERE>` 
  - `<measure_unit>` - Time unit: `YEARS`, `MONTHS`, `WEEKS`, `DAYS`, `HOURS`, `MINUTES`, `SECONDS`
- Time window - `[<start>, <end>)`

- `ASSUMING` clause - Filters data at the timestamp level (before aggregation)
- `WHERE` clause - Filters data at the timestamp level ()

#### 💡 Example

Predicting average student grade over 10-day windows:

```python
from predql.converter import TConverterPredQL
import pandas as pd

# create timestamps for temporal windows
timestamps = pd.to_datetime(["2025-01-01", "2025-01-15"])

# create temporal converter
converter = TConverterPredQL(db, timestamps)

# convert and execute temporal PredQL query
result_table = converter.convert("""
    PREDICT AVG(grades.grade, 0, 10, DAYS)
    FOR EACH students.studentId;
""")

df = result_table.df() # get dataframe object
```

## 🔧 Development

### Regenerating the Parser

```bash
./regenerate_parser.sh
```

Requires `antlr4` CLI to be installed.

### Running Linter

```bash
ruff check .
```

## 🏗️ Architecture

```
PredQL Query String
    ↓
[Lexer] → Tokens
    ↓
[Parser] → Parse Tree
    ↓
[Visitor] → Dictionary
    ↓
[Converter] → SQL Query
    ↓
[DuckDB] → Result Table
```

