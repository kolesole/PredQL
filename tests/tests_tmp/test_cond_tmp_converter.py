"""Tests for temporal converter condition handling."""

from io import StringIO

import pandas as pd
import pytest


@pytest.mark.parametrize("pql_cond", [
    ("!="),
    ("<"),
    ("<="),
    ("=="),
    (">"),
    (">=")
])
def test_num_cond_tmp(temporal_converter,
                      pql_cond):
    pql_query = f"""
        PREDICT AVG(grades.grade, 0, 10, DAYS) {pql_cond} 2.0
        FOR EACH students.studentId;
    """
    res_table = temporal_converter.convert(pql_query)
    res_df = res_table.df()
    res_fkey_col_to_pkey_table = res_table.fkey_col_to_pkey_table
    res_pkey_col = res_table.pkey_col
    res_time_col = res_table.time_col

    match pql_cond:
        case "!=":
            ref_data = """
                fk, timestamp,  label
                0,  2025-01-01, True
                1,  2025-01-01, False
                2,  2025-01-01, False
                0,  2025-01-10, True
                1,  2025-01-10, False
                2,  2025-01-10, False
            """
        case "<":
            ref_data = """
                fk, timestamp,  label
                0,  2025-01-01, True
                1,  2025-01-01, False
                2,  2025-01-01, False
                0,  2025-01-10, False
                1,  2025-01-10, False
                2,  2025-01-10, False
            """
        case "<=":
            ref_data = """
                fk, timestamp,  label
                0,  2025-01-01, True
                1,  2025-01-01, True
                2,  2025-01-01, False
                0,  2025-01-10, False
                1,  2025-01-10, True
                2,  2025-01-10, False
            """
        case "==":
            ref_data = """
                fk, timestamp,  label
                0,  2025-01-01, False
                1,  2025-01-01, True
                2,  2025-01-01, False
                0,  2025-01-10, False
                1,  2025-01-10, True
                2,  2025-01-10, False
            """
        case ">":
            ref_data = """
                fk, timestamp,  label
                0,  2025-01-01, False
                1,  2025-01-01, False
                2,  2025-01-01, False
                0,  2025-01-10, True
                1,  2025-01-10, False
                2,  2025-01-10, False
            """
        case ">=":
            ref_data = """
                fk, timestamp,  label
                0,  2025-01-01, False
                1,  2025-01-01, True
                2,  2025-01-01, False
                0,  2025-01-10, True
                1,  2025-01-10, True
                2,  2025-01-10, False
            """

    ref_df = pd.read_csv(StringIO(ref_data),
                         skipinitialspace=True,
                         parse_dates=["timestamp"],
                         na_values=['nan', 'NaN', 'NONE', ''])

    pd.testing.assert_frame_equal(res_df,
                                  ref_df,
                                  check_dtype=False,
                                  atol=1e-5)
    assert res_fkey_col_to_pkey_table is None
    assert res_pkey_col is None
    assert res_time_col == "timestamp"


@pytest.mark.parametrize("pql_cond", [
    ("CONTAINS"),
    ("NOT CONTAINS"),
    ("LIKE"),
    ("NOT LIKE"),
    ("STARTS WITH"),
    ("ENDS WITH"),
    ("=")
])
def test_str_cond_tmp(temporal_converter,
                      pql_cond):
    pql_query = f"""
        PREDICT FIRST(favSubjects.subject, 0, 10, DAYS) {pql_cond} "P"
        FOR EACH students.studentId;
    """
    res_table = temporal_converter.convert(pql_query)
    res_df = res_table.df()
    res_fkey_col_to_pkey_table = res_table.fkey_col_to_pkey_table
    res_pkey_col = res_table.pkey_col
    res_time_col = res_table.time_col

    match pql_cond:
        case "CONTAINS":
            ref_data = """
                fk, timestamp,  label
                0,  2025-01-01, True
                1,  2025-01-01, True
                2,  2025-01-01, False
                0,  2025-01-10, False
                1,  2025-01-10, True
                2,  2025-01-10, False
            """
        case "NOT CONTAINS":
            ref_data = """
                fk, timestamp,  label
                0,  2025-01-01, False
                1,  2025-01-01, False
                2,  2025-01-01, False
                0,  2025-01-10, True
                1,  2025-01-10, False
                2,  2025-01-10, False
            """
        case "LIKE":
            ref_data = """
                fk, timestamp,  label
                0,  2025-01-01, False
                1,  2025-01-01, False
                2,  2025-01-01, False
                0,  2025-01-10, False
                1,  2025-01-10, True
                2,  2025-01-10, False
            """
        case "NOT LIKE":
            ref_data = """
                fk, timestamp,  label
                0,  2025-01-01, True
                1,  2025-01-01, True
                2,  2025-01-01, False
                0,  2025-01-10, True
                1,  2025-01-10, False
                2,  2025-01-10, False
            """
        case "STARTS WITH":
            ref_data = """
                fk, timestamp,  label
                0,  2025-01-01, False
                1,  2025-01-01, True
                2,  2025-01-01, False
                0,  2025-01-10, False
                1,  2025-01-10, True
                2,  2025-01-10, False
            """
        case "ENDS WITH":
            ref_data = """
                fk, timestamp,  label
                0,  2025-01-01, False
                1,  2025-01-01, True
                2,  2025-01-01, False
                0,  2025-01-10, False
                1,  2025-01-10, True
                2,  2025-01-10, False
            """
        case "=":
            ref_data = """
                fk, timestamp,  label
                0,  2025-01-01, False
                1,  2025-01-01, False
                2,  2025-01-01, False
                0,  2025-01-10, False
                1,  2025-01-10, True
                2,  2025-01-10, False
            """

    ref_df = pd.read_csv(StringIO(ref_data),
                         skipinitialspace=True,
                         parse_dates=["timestamp"],
                         na_values=['nan', 'NaN', 'NONE', ''])

    pd.testing.assert_frame_equal(res_df,
                                  ref_df,
                                  check_dtype=False,
                                  atol=1e-5)
    assert res_fkey_col_to_pkey_table is None
    assert res_pkey_col is None
    assert res_time_col == "timestamp"


@pytest.mark.parametrize("pql_cond", [
    ("IS NOT NULL"),
    ("IS NULL")
])
def test_null_cond_tmp(temporal_converter,
                       pql_cond):
    pql_query = f"""
        PREDICT LAST(grades.grade, 0, 10, DAYS) {pql_cond}
        FOR EACH students.studentId;
    """
    res_table = temporal_converter.convert(pql_query)
    res_df = res_table.df()
    res_fkey_col_to_pkey_table = res_table.fkey_col_to_pkey_table
    res_pkey_col = res_table.pkey_col
    res_time_col = res_table.time_col

    match pql_cond:
        case "IS NULL":
            ref_data = """
                fk, timestamp,  label
                0,  2025-01-01, True
                1,  2025-01-01, False
                2,  2025-01-01, True
                0,  2025-01-10, False
                1,  2025-01-10, False
                2,  2025-01-10, True
            """
        case "IS NOT NULL":
            ref_data = """
                fk, timestamp,  label
                0,  2025-01-01, False
                1,  2025-01-01, True
                2,  2025-01-01, False
                0,  2025-01-10, True
                1,  2025-01-10, True
                2,  2025-01-10, False
            """

    ref_df = pd.read_csv(StringIO(ref_data),
                         skipinitialspace=True,
                         parse_dates=["timestamp"],
                         na_values=['nan', 'NaN', 'NONE', ''])

    pd.testing.assert_frame_equal(res_df,
                                  ref_df,
                                  check_dtype=False,
                                  atol=1e-5)
    assert res_fkey_col_to_pkey_table is None
    assert res_pkey_col is None
    assert res_time_col == "timestamp"
