"""Tests for static converter WHERE clause handling."""

import pandas as pd
import pytest


def test_where_stat(static_converter):
    pql_query = """
        PREDICT studyInf.favSubject
        FOR EACH students.studentId
        WHERE studyInf.year > 1;
    """
    res_table = static_converter.convert(pql_query)
    res_df = res_table.df()
    res_fkey_col_to_pkey_table = res_table.fkey_col_to_pkey_table
    res_pkey_col = res_table.pkey_col
    res_time_col = res_table.time_col

    sql_query = """
        SELECT
            s.studentId AS fk,
            si.favSubject AS label
        FROM
            students s
        JOIN
            studyInf si
        ON
            si.studentId = s.studentId
        WHERE
            si.year > 1
        ORDER BY
            s.studentId;
    """
    ref_df = static_converter.conn.sql(sql_query).df()

    print(res_df)
    print(ref_df)

    pd.testing.assert_frame_equal(res_df, ref_df)
    assert res_fkey_col_to_pkey_table is None
    assert res_pkey_col is None
    assert res_time_col is None


@pytest.mark.parametrize("pql_log_op, sql_log_op", [
    ("AND", "AND"),
    ("OR", "OR")
])
def test_nested_where_stat(static_converter,
                           pql_log_op,
                           sql_log_op):
    pql_query = f"""
        PREDICT studyInf.favSubject
        FOR EACH students.studentId
        WHERE studyInf.year > 1 {pql_log_op} students.name CONTAINS "k";
    """
    res_table = static_converter.convert(pql_query)
    res_df = res_table.df()
    res_fkey_col_to_pkey_table = res_table.fkey_col_to_pkey_table
    res_pkey_col = res_table.pkey_col
    res_time_col = res_table.time_col

    sql_query = f"""
        SELECT
            s.studentId AS fk,
            si.favSubject AS label
        FROM
            students s
        JOIN
            studyInf si
        ON
            si.studentId = s.studentId
        WHERE
            si.year > 1 {sql_log_op} s.name LIKE '%k%'
        ORDER BY
            s.studentId;
    """
    ref_df = static_converter.conn.sql(sql_query).df()

    print(res_df)
    print(ref_df)

    pd.testing.assert_frame_equal(res_df, ref_df)
    assert res_fkey_col_to_pkey_table is None
    assert res_pkey_col is None
    assert res_time_col is None

