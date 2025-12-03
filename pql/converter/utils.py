
def build_num_condition(cond_dict : dict):
    tmp = cond_dict["N"]
    N = float(tmp) if "." in tmp else int(tmp)

    comp_op = cond_dict["CompOp"]

    return lambda column : f"{column} {comp_op} {N}"
    


def build_str_condition(cond_dict : dict):
    s = cond_dict["String"]
    comp_op = cond_dict["CompOp"].lower()

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


def build_null_condition(cond_dict : dict):
    check_op = cond_dict["CheckOp"].upper()
    
    return lambda column : f"{column} {check_op}"


def build_aggr_func(aggr_dict : dict):
    aggr_type = aggr_dict["AggrType"].lower()
    column = aggr_dict["Column"]

    match aggr_type:
        case "avg":
            return lambda table_name : f"AVG({table_name}.{column})"
        case "count":
            return lambda table_name : f"COUNT({table_name}.{column})"
        case "count_distinct":
            return lambda table_name : f"COUNT(DISTINCT {table_name}.{column})"
        case "first":
            pass
        case "last":
            pass
        case "list_distinct":
            pass
        case "max":
            return lambda table_name : f"MAX({table_name}.{column})"
        case "min":
            return lambda table_name : f"MIN({table_name}.{column})"
        case "sum":
            return lambda table_name : f"SUM({table_name}.{column})"
        case _:
            pass


