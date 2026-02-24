"""Utility functions for building SQL conditions and aggregations."""

from collections.abc import Callable

def build_num_condition(cond_dict : dict) -> Callable[[str], str]:
    r"""Builds SQL numeric comparison condition from parsed dictionary.
    
    Args:
        cond_dict (dict): Dictionary containing 'N' (numeric value) and
            'CompOp' (comparison operator like '>', '<=', '==').
    
    Returns:
        function: Lambda that takes a column name and returns SQL condition string.
    """
    tmp = cond_dict["N"].value
    N = float(tmp) if "." in tmp else int(tmp)

    comp_op = cond_dict["CompOp"].value

    return lambda column : f"{column} {comp_op} {N}"


def build_str_condition(cond_dict : dict) -> Callable[[str], str]:
    """Builds SQL string comparison condition from parsed dictionary.
    
    Args:
        cond_dict (dict): Dictionary containing 'String' (string value) and
            'CompOp' (comparison operator like 'contains', 'starts with').
    
    Returns:
        function: Lambda that takes a column name and returns SQL condition string.
    """
    s = cond_dict["String"].value.strip("'\"")
    comp_op = cond_dict["CompOp"].value.lower()

    match comp_op:
        case "contains":
            return lambda column : f"{column} LIKE '%{s}%'"
        case "not contains":
            return lambda column : f"{column} NOT LIKE '%{s}%'"
        case "like":
            return lambda column : f"{column} LIKE '{s}'"
        case "not like":
            return lambda column : f"{column} NOT LIKE '{s}'"
        case "starts with":
            return lambda column : f"{column} LIKE '{s}%'"
        case "ends with":
            return lambda column : f"{column} LIKE '%{s}'"
        case "=":
            return lambda column : f"{column} = '{s}'"
        case _:
            pass


def build_null_condition(cond_dict : dict) -> Callable[[str], str]:
    """Builds SQL NULL check condition from parsed dictionary.
    
    Args:
        cond_dict (dict): Dictionary containing 'CheckOp' (NULL, IS_NULL).
    
    Returns:
        function: Lambda that takes a column name and returns SQL condition string.
    """
    check_op = cond_dict["CheckOp"].value.upper()

    return lambda column : f"{column} {check_op}"


def build_aggr_func(aggr_dict   : dict, 
                    fk          : str=None, 
                    time_column : str=None, 
                    ppk         : str=None) -> Callable[[str], str]:
    """Build SQL aggregation function from parsed dictionary.
    
    For temporal aggregations (LIST_DISTINCT with time_column), generates SQL subquery which
    returns list sorted by frequency for all (*fk*, *timestamp*) pairs.
    
    Args:
        aggr_dict (dict): Dictionary containing 'AggrType' (aggregation type) and 'Column' (column to aggregate).  
            For temporal LIST_DISTINCT, also contains 'Table', 'Start', 'End', and 'MeasureUnit'.
        fk (str, optional): Foreign key column name for temporal aggregations.
        time_column (str, optional): Time column name for temporal aggregations.
        ppk (str, optional): Parent primary key column name for temporal aggregations.
    
    Returns:
        function: Lambda that takes a table name and returns SQL aggregation expression.
    """
    aggr_type = aggr_dict["AggrType"].value.lower()
    column = aggr_dict["Column"].value

    match aggr_type:
        case "avg":
            return lambda table: f"AVG({table}.{column})"
        case "count":
            return lambda table: f"COUNT({table}.{column})"
        case "count_distinct":
            return lambda table: f"COUNT(DISTINCT {table}.{column})"
        case "first":
            return lambda table : f"ARRAY_AGG({table}.{column} ORDER BY {table}.{time_column} ASC)[1]"
        case "last":
            return lambda table : f"ARRAY_AGG({table}.{column} ORDER BY {table}.{time_column} DESC)[1]"
        case "list_distinct":
            if time_column:
                # Temporal LIST_DISTINCT: aggregate values within time window,
                # ordered by frequency (most frequent first)
                in_table = aggr_dict["Table"].value
                start = int(aggr_dict["Start"].value)
                end = int(aggr_dict["End"].value)
                measure_unit = aggr_dict["MeasureUnit"].value.upper().removesuffix("S")

                return lambda table : (
                     "(\n"
                     "SELECT\n"
                     "    ARRAY_AGG(freq_tbl.val ORDER BY freq_tbl.freq DESC)\n"
                     "FROM (\n"
                     "    SELECT\n"
                    f"        in_tbl.{column} AS val,\n"
                    f"        COUNT(*) AS freq\n"
                     "    FROM\n"
                    f"        {in_table} in_tbl\n"
                     "    WHERE\n"
                    f"        in_tbl.{time_column} >= time.timestamp + INTERVAL '{start} {measure_unit}'\n"
                     "    AND\n"
                    f"        in_tbl.{time_column} <  time.timestamp + INTERVAL '{end} {measure_unit}'\n"
                    f"    AND\n"
                    f"        in_tbl.{fk} = parent.{ppk}\n"
                    f"    GROUP BY in_tbl.{column}\n"
                     "    ) freq_tbl\n"
                     ")"
                )
            else:
                # Static LIST_DISTINCT: simple array aggregation of distinct values
                return lambda table : f"ARRAY_AGG(DISTINCT {table}.{column})"
        case "max":
            return lambda table : f"MAX({table}.{column})"
        case "min":
            return lambda table : f"MIN({table}.{column})"
        case "sum":
            return lambda table : f"SUM({table}.{column})"
        case _:
            pass


def get_div_line(message : str) -> str:
    """Generate a division line with message for SQL formatting.
    
    Creates a SQL comment line with a message.
    
    Args:
        message (str): Message to include in the division line.
    
    Returns:
        out (None):
    """
    return f"{'--' * 3}{message}{'--' * 3}"
