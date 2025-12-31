# PredQL 

**PredQL** (Predictive Query Language) is a Python framework that simplifies working with databases for **Relational Deep Learning (RDL)**.

It lets you write shorter, more expressive queries by abstracting temporal joins and complex aggregations.

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

- Every table you reference must contain a `<foreign_key>` that matches the `<entity_table>` `<primary_key>`

- `<condition>` design:

    ```sql
    <table>.<column> <num_condition>|<str_condition>|<null_condition>
    ```
    | Category    | Operators | Right side |
    | :---        | :---      | :--- |
    | **Numeric** | `!=`, `<`, `<=`, `==`, `>`, `>=` | NUMBER
    | **String** | `CONTAINS`, `NOT CONTAINS`, `LIKE`, `NOT LIKE`, `STARTS WITH`, `ENDS WITH`, `=` | STRING
    | **Nullability** | `IS NULL`, `IS NOT NULL` | |

- Static converter returns a table with:
    - `fk` - `<primary_key>` from `<entity_table>`
    - `label` - predicted value

#### 💡 Examples 

```python
from predql.converter import SConverterPredQL
from relbench.base import Database

# load your database with tables
db = Database(...)

# create converter
converter = SConverterPredQL(db)

# predicting student favorite subject
example_query1 = """                   
    PREDICT studentInf.favSubject     
    FOR EACH students.studentId;     
"""                                   
result_table1 = converter.convert(example_query1)

# predicting student favorite subject for students older than 20
example_query2 = """                   
    PREDICT studentInf.favSubject     
    FOR EACH students.studentId
    WHERE studentInf.age > 20;     
"""                                   
result_table2 = converter.convert(example_query2)

# get dataframes
df1 = result_table1.df()
df2 = result_table2.df()
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

- Every table you reference must contain a `<foreign_key>` that matches the `<entity_table>` `<primary_key>`

- `<condition>` design:

    ```sql
    <aggregation> <num_condition>|<str_condition>|<null_condition>
    ```
    `<num_condition>`, `<str_condition>`, `<null_condition>` - The same as in static

- `<aggregation>` design:

    ```sql
    <aggr_func>(<target_table>.<target_column>, <start>, <end>, <measure_unit>) [<RANK TOP K>|<CLASSIFY>]
    ```
    `<RANK TOP K>` and `<CLASSIFY>` apply only to `LIST_DISTINCT`; `K` must be a positive integer\
    `<RANK TOP K>` returns the first `K` elements (by frequency), `<CLASSIFY>` or omitting both returns all elements
    
- Available aggregation functions:

    | Function | Description | Can be used in condition
    | :--- | :--- | :--- |
    | `AVG` | Average value| ✅
    | `MAX` | Maximum value| ✅
    | `MIN` | Minimum value| ✅
    | `SUM` | Sum of values| ✅
    | `COUNT` | Count of non-null values| ✅
    | `COUNT_DISTINCT` | Count of distinct values| ✅
    | `FIRST` | First value (ordered by time)| ✅
    | `LAST` | Last value (ordered by time)| ✅
    | `LIST_DISTINCT` | List of distinct values ordered by count| ❌

- Time window parameters:

    - `<start>` must be `≤ 0` for `ASSUMING` and `≥ 0` for `PREDICT`/`WHERE`
    - `<end>` must be `≤ 0` for `ASSUMING` and `≥ 0` for `PREDICT`/`WHERE`
    - `<measure_unit>`: `YEARS`, `MONTHS`, `WEEKS`, `DAYS`, `HOURS`, `MINUTES`, `SECONDS`

- Time window is half-open: `[<start>, <end>)`

- `ASSUMING` filters past context (per timestamp)

- `WHERE` filters future context (per timestamp)

- Temporal converter returns a table with:

    - `fk` - `<primary_key>` from `<entity_table>`
    - `timestamp` - timestamps you provide to the converter
    - `label` - predicted value

#### 💡 Example

```python
from predql.converter import TConverterPredQL
from relbench.base import Database
import pandas as pd

# create timestamps for temporal windows
timestamps = pd.to_datetime(["2025-01-01", "2025-01-15"])

# load your database with tables
db = Database(...)

# create temporal converter
converter = TConverterPredQL(db, timestamps)

# predicting average student grade over 10-day windows
example_query1 = """
    PREDICT AVG(grades.grade, 0, 10, DAYS)
    FOR EACH students.studentId;
"""
result_table1 = converter.convert(example_query1)

# predicting average student grade over 10-day windows
# for students whose average grade in previous 10 days is > 2
# and whose average grade in the subsequent 10 days is < 3
example_query2 = """
    PREDICT AVG(grades.grade, 0, 10, DAYS)
    FOR EACH students.studentId
    ASSUMING AVG(grades.grade, -10, 0, DAYS) > 2
    WHERE AVG(grades.grade, 10, 20, DAYS) < 3;
"""
result_table2 = converter.convert(example_query2)

# get dataframes
df1 = result_table1.df()
df2 = result_table2.df()
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

## 🔧 Development

### Install `uv`

- macOS & Linux

    ```bash
    wget -qO- https://astral.sh/uv/install.sh | sh
    ```

- Windows

    ```bash
    powershell -ExecutionPolicy ByPass -c "irm https://astral.sh/uv/install.ps1 | iex"
    ```

### Install dependencies

```bash
uv sync --all-extras
```

### Regenerating the Parser

If you change the lexer or parser (`*.g4`), regenerate the ANTLR outputs from the repo root:

```bash
./regenerate_parser.sh
```

### Running Linter

```bash
ruff check .
```
