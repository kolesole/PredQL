"""Tests for temporal converter aggregation functions."""

import json
from io import StringIO

import pandas as pd
import pytest


@pytest.mark.parametrize("pql_aggr", [
    ("AVG"),
    ("MAX"),
    ("MIN"),
    ("SUM"),
    ("COUNT"),
    ("COUNT_DISTINCT"),
    ("FIRST"),
    ("LAST")
])
def test_aggr_tmp(temporal_converter,
                  pql_aggr):
    pql_query = f"""
        PREDICT {pql_aggr}(grades.grade, 0, 10, DAYS)
        FOR EACH students.studentId;
    """
    res_table = temporal_converter.convert(pql_query, execute=True)
    res_df = res_table.df
    res_fkey_col_to_pkey_table = res_table.fkey_col_to_pkey_table
    res_pkey_col = res_table.pkey_col
    res_time_col = res_table.time_col

    match pql_aggr:
        case "AVG":
            ref_data = """
                fk, timestamp,  label
                0,  2025-01-01, 1.6
                1,  2025-01-01, 2.0
                0,  2025-01-10, 4.0
                1,  2025-01-10, 2.0
            """
        case "MAX":
            ref_data = """
                fk, timestamp,  label
                0,  2025-01-01, 2.0
                1,  2025-01-01, 2.0
                0,  2025-01-10, 4.0
                1,  2025-01-10, 4.0
            """
        case "MIN":
            ref_data = """
                fk, timestamp,  label
                0,  2025-01-01, 1.0
                1,  2025-01-01, 2.0
                0,  2025-01-10, 4.0
                1,  2025-01-10, 1.0
            """
        case "SUM":
            ref_data = """
                fk, timestamp,  label
                0,  2025-01-01, 8.0
                1,  2025-01-01, 2.0
                0,  2025-01-10, 4.0
                1,  2025-01-10, 6.0
            """
        case "COUNT":
            ref_data = """
                fk, timestamp,  label
                0,  2025-01-01, 5.0
                1,  2025-01-01, 1.0
                2,  2025-01-01, 0.0
                0,  2025-01-10, 1.0
                1,  2025-01-10, 3.0
                2,  2025-01-10, 0.0
            """
        case "COUNT_DISTINCT":
            ref_data = """
                fk, timestamp,  label
                0,  2025-01-01, 2.0
                1,  2025-01-01, 1.0
                2,  2025-01-01, 0.0
                0,  2025-01-10, 1.0
                1,  2025-01-10, 2.0
                2,  2025-01-10, 0.0
            """
        case "FIRST":
            ref_data = """
                fk, timestamp,  label
                0,  2025-01-01, 1.0
                1,  2025-01-01, 2.0
                0,  2025-01-10, 4.0
                1,  2025-01-10, 1.0
            """
        case "LAST":
            ref_data = """
                fk, timestamp,  label
                1,  2025-01-01, 2.0
                0,  2025-01-10, 4.0
                1,  2025-01-10, 4.0
            """

    ref_df = pd.read_csv(StringIO(ref_data),
                             skipinitialspace=True,
                             parse_dates=["timestamp"],
                             na_values=['nan', 'NaN', 'NONE', ''])

    pd.testing.assert_frame_equal(res_df,
                                  ref_df,
                                  check_dtype=False,
                                  atol=1e-5)

    assert res_fkey_col_to_pkey_table == {"fk" : "students"}
    assert res_pkey_col is None
    assert res_time_col == "timestamp"

@pytest.mark.parametrize("list_distinct_op", [
    (""),
    ("CLASSIFY"),
    ("RANK TOP 3")
])
def test_list_distinct_tmp(temporal_converter,
                           list_distinct_op):
    pql_query = f"""
        PREDICT LIST_DISTINCT(grades.grade, 0, 10, DAYS) {list_distinct_op}
        FOR EACH students.studentId;
    """
    res_table = temporal_converter.convert(pql_query, execute=True)
    res_df = res_table.df

    def normalize_label(value):
        if isinstance(value, str):
            items = json.loads(value)
        elif hasattr(value, "tolist"):
            items = value.tolist()
        else:
            items = list(value)

        return sorted(item if pd.notna(item) else 0.0 for item in items)

    res_df["label"] = res_df["label"].apply(normalize_label)
    res_fkey_col_to_pkey_table = res_table.fkey_col_to_pkey_table
    res_pkey_col = res_table.pkey_col
    res_time_col = res_table.time_col

    match list_distinct_op:
        case "" | "CLASSIFY" | "RANK TOP 3":
            ref_data = [
                {"fk": 0, "timestamp": "2025-01-01", "label": [1.0, 2.0]}, # [2, 1]
                {"fk": 1, "timestamp": "2025-01-01", "label": [2.0]},
                {"fk": 0, "timestamp": "2025-01-10", "label": [4.0]},
                {"fk": 1, "timestamp": "2025-01-10", "label": [1.0, 4.0]}
            ]

    ref_df = pd.DataFrame(ref_data)
    ref_df["timestamp"] = pd.to_datetime(ref_df["timestamp"])

    actual = json.loads(res_df.to_json(orient="records", double_precision=5))
    expected = json.loads(ref_df.to_json(orient="records", double_precision=5))

    assert actual == expected
    assert res_fkey_col_to_pkey_table == {"fk" : "students"}
    assert res_pkey_col is None
    assert res_time_col == "timestamp"

