"""Tests for static converter condition handling."""

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
def test_num_cond_tmp(static_converter,
                      pql_cond):
    pql_query = f"""
        PREDICT studyInf.studyYear {pql_cond} 3
        FOR EACH students.studentId;
    """
    res_table = static_converter.convert(pql_query)
    res_df = res_table.df()
    res_fkey_col_to_pkey_table = res_table.fkey_col_to_pkey_table
    res_pkey_col = res_table.pkey_col
    res_time_col = res_table.time_col

    match pql_cond:
        case "!=":
            ref_data = """
                fk, label
                0,  False
                1,  True
                2,  False
            """
        case "<":
            ref_data = """
                fk, label
                0,  False
                1,  False
                2,  False
            """
        case "<=":
             ref_data = """
                fk, label
                0,  True
                1,  False
                2,  False
            """
        case "==":
            ref_data = """
                fk, label
                0,  True
                1,  False
                2,  False
            """
        case ">":
            ref_data = """
                fk, label
                0,  False
                1,  True
                2,  False
            """
        case ">=":
            ref_data = """
                fk, label
                0,  True
                1,  True
                2,  False
            """

    ref_df = pd.read_csv(StringIO(ref_data), 
                         skipinitialspace=True, 
                         na_values=['nan', 'NaN', 'NONE', ''])
    
    pd.testing.assert_frame_equal(res_df, 
                                  ref_df, 
                                  check_dtype=False,
                                  atol=1e-5)
    assert res_fkey_col_to_pkey_table is None
    assert res_pkey_col is None
    assert res_time_col is None


@pytest.mark.parametrize("pql_cond", [
    ("CONTAINS"),
    ("NOT CONTAINS"),
    ("LIKE"),
    ("NOT LIKE"),
    ("STARTS WITH"),
    ("ENDS WITH"),
    ("=")
])
def test_str_cond_tmp(static_converter,
                      pql_cond):
    pql_query = f"""
        PREDICT studyInf.mainInterest {pql_cond} "S"
        FOR EACH students.studentId;
    """
    res_table = static_converter.convert(pql_query)
    res_df = res_table.df()
    res_fkey_col_to_pkey_table = res_table.fkey_col_to_pkey_table
    res_pkey_col = res_table.pkey_col
    res_time_col = res_table.time_col

    match pql_cond:
        case "CONTAINS":
            ref_data = """
                fk, label
                0,  False
                1,  True
                2,  True
            """
        case "NOT CONTAINS":
            ref_data = """
                fk, label
                0,  True
                1,  False
                2,  False
            """
        case "LIKE":
            ref_data = """
                fk, label
                0,  False
                1,  False
                2,  False
            """
        case "NOT LIKE":
            ref_data = """
                fk, label
                0,  True
                1,  True
                2,  True
            """
        case "STARTS WITH":
            ref_data = """
                fk, label
                0,  False
                1,  False
                2,  True
            """
        case "ENDS WITH":
            ref_data = """
                fk, label
                0,  False
                1,  True
                2,  False
            """
        case "=":
            ref_data = """
                fk, label
                0,  False
                1,  False
                2,  False
            """

    ref_df = pd.read_csv(StringIO(ref_data), 
                         skipinitialspace=True, 
                         na_values=['nan', 'NaN', 'NONE', ''])
    
    pd.testing.assert_frame_equal(res_df, 
                                  ref_df, 
                                  check_dtype=False,
                                  atol=1e-5)
    assert res_fkey_col_to_pkey_table is None
    assert res_pkey_col is None
    assert res_time_col is None


@pytest.mark.parametrize("pql_cond", [
    ("IS NOT NULL"),
    ("IS NULL")
])
def test_null_cond_tmp(static_converter,
                       pql_cond):
    pql_query = f"""
        PREDICT studyInf.studyYear {pql_cond}
        FOR EACH students.studentId;
    """
    res_table = static_converter.convert(pql_query)
    res_df = res_table.df()
    res_fkey_col_to_pkey_table = res_table.fkey_col_to_pkey_table
    res_pkey_col = res_table.pkey_col
    res_time_col = res_table.time_col

    match pql_cond:
        case "IS NULL":
            ref_data = """
                fk, label
                0,  False
                1,  False
                2,  True
            """
        case "IS NOT NULL":
            ref_data = """
                fk, label
                0,  True
                1,  True
                2,  False
            """

    ref_df = pd.read_csv(StringIO(ref_data), 
                         skipinitialspace=True, 
                         na_values=['nan', 'NaN', 'NONE', ''])
    
    pd.testing.assert_frame_equal(res_df, 
                                  ref_df, 
                                  check_dtype=False,
                                  atol=1e-5)
    assert res_fkey_col_to_pkey_table is None
    assert res_pkey_col is None
    assert res_time_col is None