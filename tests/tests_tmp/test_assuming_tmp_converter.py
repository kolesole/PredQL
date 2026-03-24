"""Tests for temporal converter ASSUMING clause handling."""

from io import StringIO

import pandas as pd


def test_assuming_tmp(temporal_converter):
    pql_query = """
        PREDICT AVG(grades.grade, 0, 10, DAYS)
        FOR EACH students.studentId
        ASSUMING LAST(grades.grade, -10, 0, DAYS) IS NULL;
    """
    res_table = temporal_converter.convert(pql_query, execute=True)
    res_df = res_table.df
    res_fkey_col_to_pkey_table = res_table.fkey_col_to_pkey_table
    res_pkey_col = res_table.pkey_col
    res_time_col = res_table.time_col

    ref_data = """
        fk, timestamp,  label
        0,  2025-01-01, 1.6
        1,  2025-01-01, 2.0
        0,  2025-01-10, 4.0
    """

    print(res_df)

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
