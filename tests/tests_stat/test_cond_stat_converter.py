"""Tests for static converter condition handling."""

import pandas as pd
import pytest


@pytest.mark.parametrize("pql_cond, sql_cond", [
    ("!=", "!="),
    ("<", "<"),
    ("<=", "<="),
    ("==", "="),
    (">", ">"),
    (">=", ">=")
])
def test_num_cond_tmp(static_converter,
                      pql_cond,
                      sql_cond):
    pql_query = f"""
        PREDICT studyInf.year {pql_cond} 2.5
        FOR EACH students.studentId;
    """
    res_table = static_converter.convert(pql_query)
    res_df = res_table.df()
    res_fkey_col_to_pkey_table = res_table.fkey_col_to_pkey_table
    res_pkey_col = res_table.pkey_col
    res_time_col = res_table.time_col

    sql_query = f"""
        SELECT
            s.studentId AS fk,
            CASE
                WHEN si.year {sql_cond} 2.5 THEN true
                ELSE false
            END AS label
        FROM
            students s
        LEFT JOIN
            studyInf si
        ON
            si.studentId = s.studentId
        ORDER BY
            s.studentId;
    """
    ref_df = static_converter.conn.sql(sql_query).df()

    pd.testing.assert_frame_equal(res_df, ref_df)
    assert res_fkey_col_to_pkey_table is None
    assert res_pkey_col is None
    assert res_time_col is None

@pytest.mark.parametrize("pql_cond, sql_cond", [
    ("CONTAINS", lambda s : f"LIKE '%{s}%'"),
    ("NOT CONTAINS", lambda s : f"NOT LIKE '%{s}%'"),
    ("LIKE", lambda s : f"LIKE '{s}'"),
    ("NOT LIKE", lambda s : f"NOT LIKE '{s}'"),
    ("STARTS WITH", lambda s : f"LIKE '{s}%'"),
    ("ENDS WITH", lambda s : f"LIKE '%{s}'"),
    ("=", lambda s : f"= '{s}'")
])
def test_str_cond_tmp(static_converter,
                      pql_cond,
                      sql_cond):
    pql_query = f"""
        PREDICT studyInf.favSubject {pql_cond} "S"
        FOR EACH students.studentId;
    """
    res_table = static_converter.convert(pql_query)
    res_df = res_table.df()
    res_fkey_col_to_pkey_table = res_table.fkey_col_to_pkey_table
    res_pkey_col = res_table.pkey_col
    res_time_col = res_table.time_col

    sql_query = f"""
        SELECT
            s.studentId AS fk,
            CASE
                WHEN si.favSubject {sql_cond("S")} THEN true
                ELSE false
            END AS label
        FROM
            students s
        LEFT JOIN
            studyInf si
        ON
            si.studentId = s.studentId
        ORDER BY
            s.studentId;
    """
    ref_df = static_converter.conn.sql(sql_query).df()

    pd.testing.assert_frame_equal(res_df, ref_df)
    assert res_fkey_col_to_pkey_table is None
    assert res_pkey_col is None
    assert res_time_col is None


@pytest.mark.parametrize("pql_cond, sql_cond", [
    ("IS NOT NULL", "IS NOT NULL"),
    ("IS NULL", "IS NULL")
])
def test_null_cond_tmp(static_converter,
                       pql_cond,
                       sql_cond):
    pql_query = f"""
        PREDICT studyInf.favSubject {pql_cond}
        FOR EACH students.studentId;
    """
    res_table = static_converter.convert(pql_query)
    res_df = res_table.df()
    res_fkey_col_to_pkey_table = res_table.fkey_col_to_pkey_table
    res_pkey_col = res_table.pkey_col
    res_time_col = res_table.time_col

    sql_query = f"""
        SELECT
            s.studentId AS fk,
            CASE
                WHEN si.favSubject {sql_cond} THEN true
                ELSE false
            END AS label
        FROM
            students s
        LEFT JOIN
            studyInf si
        ON
            si.studentId = s.studentId
        ORDER BY
            s.studentId;
    """
    ref_df = static_converter.conn.sql(sql_query).df()

    pd.testing.assert_frame_equal(res_df, ref_df)
    assert res_fkey_col_to_pkey_table is None
    assert res_pkey_col is None
    assert res_time_col is None
