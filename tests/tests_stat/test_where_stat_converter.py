"""Tests for static converter WHERE clause handling."""

from io import StringIO

import pandas as pd
import pytest


def test_where_stat(static_converter):
    pql_query = """
        PREDICT studyInf.mainInterest
        FOR EACH students.studentId
        WHERE studyInf.studyYear <= 3;
    """
    res_table = static_converter.convert(pql_query)
    res_df = res_table.df()
    res_fkey_col_to_pkey_table = res_table.fkey_col_to_pkey_table
    res_pkey_col = res_table.pkey_col
    res_time_col = res_table.time_col

    ref_data = """
        fk, label
        0,  AI
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


@pytest.mark.parametrize("pql_op", [
    ("AND"),
    ("OR")
])
def test_nested_where_stat(static_converter,
                           pql_op):
    pql_query = f"""
        PREDICT studyInf.mainInterest
        FOR EACH students.studentId
        WHERE (studyInf.studyYear >= 1 {pql_op} students.name CONTAINS "e")
        OR studyInf.studyYear IS NULL;
    """
    res_table = static_converter.convert(pql_query)
    res_df = res_table.df()
    res_fkey_col_to_pkey_table = res_table.fkey_col_to_pkey_table
    res_pkey_col = res_table.pkey_col
    res_time_col = res_table.time_col

    match pql_op:
        case "AND":
            ref_data = """
                fk, label
                0,  AI
                2,  SI
            """
        case "OR":
            ref_data = """
                fk, label
                0,  AI
                1,  DS
                2,  SI
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

