
def gen_num_filter(cond_dict : dict):
    tmp = cond_dict["N"]
    N = float(tmp) if "." in tmp else int(tmp)

    comp_op = cond_dict["CompOp"]
    match comp_op:
        case "!=":
            return lambda df, col : df[col.astype(float) != N]
        case "<":
            return lambda df, col : df[col.astype(float) < N]
        case "<=":
            return lambda df, col : df[col.astype(float) <= N]
        case "==":
            return lambda df, col : df[col.astype(float) == N]
        case ">":
            return lambda df, col : df[col.astype(float) > N]
        case ">=":
            return lambda df, col : df[col.astype(float) >= N]
        case _:
            pass


def gen_str_filter(cond_dict : dict):
    s = cond_dict["String"]
    print(s)
    # import re
    # has_space = bool(re.search(r"\s", s))
    # print(has_space)

    comp_op = cond_dict["CompOp"].lower()
    match comp_op:
        case "not like":
            return lambda df, col : df[~col.astype(str).str.match(s)]
        case "not contains":
            return lambda df, col : df[~col.astype(str).str.contains(s, na=False)]
        case "ends with":
            return lambda df, col : df[col.astype(str).str.endswith(s, na=False)]
        case "starts with":
            return lambda df, col : df[col.astype(str).str.startswith(s, na=False)]
        case "like":
            return lambda df, col : df[col.astype(str).str.match(s)]
        case "contains":
            return lambda df, col : df[col.astype(str).str.contains(s, na=False)]
        case "=":
            def _cond(df, col):
                return df[col] == s
            return _cond
        case _:
            pass


def gen_null_filter(cond_dict : dict):
    check_op = cond_dict["CheckOp"].lower()
    match check_op:
        case "is not null":
            return lambda df, col : df[col.isna()]
        case "is null":
            return lambda df, col : df[col.notna()]
        case _:
            pass


def gen_aggr_func(aggr_type):
    match aggr_type:
        case "avg":
            return lambda series : series.mean()
        case "count":
            return lambda series : series.count()
        case "count_distinct":
            return lambda series : series.nunique()
        case "first":
            pass
        case "last":
            pass
        case "list_distinct":
            pass
        case "max":
            return lambda series : series.max()
        case "min":
            return lambda series : series.min()
        case "sum":
            return lambda series : series.sum()
        case _:
            pass


