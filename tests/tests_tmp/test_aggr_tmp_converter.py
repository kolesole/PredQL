"""Tests for temporal converter aggregation functions."""

import pandas as pd
import pytest


@pytest.mark.parametrize("pql_aggr, sql_aggr", [
    ("AVG", "AVG"),
    ("MAX", "MAX"),
    ("MIN", "MIN"),
    ("SUM", "SUM")
])
def test_num_aggr_tmp(temporal_converter,
                      pql_aggr,
                      sql_aggr):
    pql_query = f"""
        PREDICT {pql_aggr}(grades.grade, 0, 10, DAYS)
        FOR EACH students.studentId;
    """
    res_table = temporal_converter.convert(pql_query)
    res_df = res_table.df()
    res_fkey_col_to_pkey_table = res_table.fkey_col_to_pkey_table
    res_pkey_col = res_table.pkey_col
    res_time_col = res_table.time_col

    sql_query = f"""
        SELECT
            s.studentId AS fk,
            t.timestamp AS timestamp,
            {sql_aggr}(g.grade) AS label
        FROM
            students s
        CROSS JOIN
            timestamp_df t
        LEFT JOIN
            grades g
        ON
            g.studentId = s.studentId
        AND
            g.date >= t.timestamp + INTERVAL '0 DAY'
        AND
            g.date < t.timestamp + INTERVAL '10 DAY'
        GROUP BY
            s.studentId, t.timestamp
        ORDER BY
            t.timestamp, s.studentId;
    """
    ref_df = temporal_converter.conn.sql(sql_query).df()
    ref_time_col = "timestamp"

    pd.testing.assert_frame_equal(res_df, ref_df, check_dtype=False)
    assert res_fkey_col_to_pkey_table is None
    assert res_pkey_col is None
    assert res_time_col is ref_time_col

#TODO: FIX -> PQLConverter returns NULL, SQL returns 0
@pytest.mark.parametrize("pql_aggr, sql_aggr", [
    ("COUNT", lambda table, column : f"COUNT({table}.{column})"),
    ("COUNT_DISTINCT", lambda table, column : f"COUNT(DISTINCT {table}.{column})")
])
def test_count_aggr_tmp(temporal_converter,
                        pql_aggr,
                        sql_aggr):
    pql_query = f"""
        PREDICT {pql_aggr}(grades.grade, 0, 10, DAYS)
        FOR EACH students.studentId;
    """
    res_table = temporal_converter.convert(pql_query)
    res_df = res_table.df()
    res_fkey_col_to_pkey_table = res_table.fkey_col_to_pkey_table
    res_pkey_col = res_table.pkey_col
    res_time_col = res_table.time_col

    sql_query = f"""
        SELECT
            s.studentId AS fk,
            t.timestamp AS timestamp,
            {sql_aggr("g", "grade")} AS label
        FROM
            students s
        CROSS JOIN
            timestamp_df t
        LEFT JOIN
            grades g
        ON
            g.studentId = s.studentId
        AND
            g.date >= t.timestamp + INTERVAL '0 DAY'
        AND
            g.date < t.timestamp + INTERVAL '10 DAY'
        GROUP BY
            s.studentId, t.timestamp
        ORDER BY
            t.timestamp, s.studentId;
    """
    ref_df = temporal_converter.conn.sql(sql_query).df()
    ref_time_col = "timestamp"

    print(temporal_converter.db.table_dict["grades"])
    print(res_df)
    print(ref_df)

    pd.testing.assert_frame_equal(res_df, ref_df, check_dtype=False)
    assert res_fkey_col_to_pkey_table is None
    assert res_pkey_col is None
    assert res_time_col == ref_time_col

@pytest.mark.parametrize("pql_aggr, sql_aggr", [
    ("FIRST", lambda table, column, time_column : f"ARRAY_AGG({table}.{column} ORDER BY {table}.{time_column})[1]"),
    ("LAST", lambda table, column, time_column : f"ARRAY_AGG({table}.{column} ORDER BY {table}.{time_column} DESC)[1]")
])
def test_array_aggr_tmp(temporal_converter,
                        pql_aggr,
                        sql_aggr):
    pql_query = f"""
        PREDICT {pql_aggr}(grades.grade, 0, 10, DAYS)
        FOR EACH students.studentId;
    """
    res_table = temporal_converter.convert(pql_query)
    res_df = res_table.df()
    res_fkey_col_to_pkey_table = res_table.fkey_col_to_pkey_table
    res_pkey_col = res_table.pkey_col
    res_time_col = res_table.time_col

    sql_query = f"""
        SELECT
            s.studentId AS fk,
            t.timestamp AS timestamp,
            {sql_aggr("g", "grade", "date")} AS label
        FROM
            students s
        CROSS JOIN
            timestamp_df t
        LEFT JOIN
            grades g
        ON
            g.studentId = s.studentId
        AND
            g.date >= t.timestamp + INTERVAL '0 DAY'
        AND
            g.date < t.timestamp + INTERVAL '10 DAY'
        GROUP BY
            s.studentId, t.timestamp
        ORDER BY
            t.timestamp, s.studentId;
    """
    ref_df = temporal_converter.conn.sql(sql_query).df()
    ref_time_col = "timestamp"

    print(temporal_converter.db.table_dict["grades"])
    print(res_df)
    print(ref_df)

    pd.testing.assert_frame_equal(res_df, ref_df, check_dtype=False)
    assert res_fkey_col_to_pkey_table is None
    assert res_pkey_col is None
    assert res_time_col == ref_time_col

#TODO: FIX AN INCOMPREHENSIBLE ERROR!!!!!!!!!!!!!!!!
def test_list_distinct_tmp(temporal_converter):
    pql_query = """
        PREDICT LIST_DISTINCT(grades.grade, 0, 15, DAYS)
        FOR EACH students.studentId;
    """
    res_table = temporal_converter.convert(pql_query)
    res_df = res_table.df()
    res_fkey_col_to_pkey_table = res_table.fkey_col_to_pkey_table
    res_pkey_col = res_table.pkey_col
    res_time_col = res_table.time_col

    sql_query = """
        SELECT
            s.studentId AS fk,
            t.timestamp AS timestamp,
            (
            SELECT
                ARRAY_AGG(val ORDER BY freq DESC)
            FROM (
                SELECT
                    inner_g.grade AS val,
                    COUNT(*) AS freq
                FROM
                    grades inner_g
                WHERE
                    inner_g.date >= t.timestamp + INTERVAL '0 DAYS'
                AND
                    inner_g.date < t.timestamp + INTERVAL '15 DAYS'
                AND
                    inner_g.studentId = s.studentId
                GROUP BY
                    inner_g.grade) frequency
            ) AS label
        FROM
            students s
        CROSS JOIN
            timestamp_df t
        GROUP BY
            s.studentId, t.timestamp
        ORDER BY
            t.timestamp, s.studentId;
    """
    ref_df = temporal_converter.conn.sql(sql_query).df()
    ref_time_col = "timestamp"

    print(temporal_converter.db.table_dict["grades"])
    print(res_df)
    print(ref_df)

    pd.testing.assert_frame_equal(res_df, ref_df)
    assert res_fkey_col_to_pkey_table is None
    assert res_pkey_col is None
    assert res_time_col == ref_time_col


