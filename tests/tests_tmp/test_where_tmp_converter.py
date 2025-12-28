"""Tests for temporal converter WHERE clause handling."""

import pandas as pd
import pytest


def test_stat_where_tmp(temporal_converter):
    pql_query = """
        PREDICT AVG(grades.grade WHERE studyInf.favSubject CONTAINS "S", 0, 10, DAYS)
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
            AVG(g.grade) AS label
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
        JOIN
            studyInf si
        ON
            si.studentId = s.studentId
        AND
            si.favSubject LIKE '%S%'
        GROUP BY
            s.studentId, t.timestamp
        ORDER BY
            t.timestamp, s.studentId;
    """
    ref_df = temporal_converter.conn.sql(sql_query).df()
    ref_time_col = "timestamp"

    print(res_df)
    print(ref_df)

    pd.testing.assert_frame_equal(res_df, ref_df)
    assert res_fkey_col_to_pkey_table is None
    assert res_pkey_col is None
    assert res_time_col == ref_time_col


def test_common_simple_where_tmp(temporal_converter):
    pql_query = """
        PREDICT AVG(grades.grade, 5, 10, DAYS)
        FOR EACH students.studentId
        WHERE AVG(grades.grade, 0, 5, DAYS) < 2.5;
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
            future.avg  AS label
        FROM
            students s
        CROSS JOIN
            timestamp_df t
        LEFT JOIN (
            SELECT
                inner_g.studentId,
                inner_t.timestamp,
                AVG(inner_g.grade) as avg
            FROM
                grades inner_g,
                timestamp_df inner_t
            WHERE
                inner_g.date >= inner_t.timestamp + INTERVAL '0 DAY'
            AND
                inner_g.date < inner_t.timestamp + INTERVAL '5 DAY'
            GROUP BY
                inner_g.studentId, inner_t.timestamp
        ) past
        ON
            past.studentId = s.studentId
        AND
            past.timestamp = t.timestamp
        LEFT JOIN (
            SELECT
                inner_g.studentId,
                inner_t.timestamp,
                AVG(inner_g.grade) as avg
            FROM
                grades inner_g,
                timestamp_df inner_t
            WHERE
                inner_g.date >= inner_t.timestamp + INTERVAL '5 DAY'
            AND
                inner_g.date < inner_t.timestamp + INTERVAL '10 DAY'
            GROUP BY
                inner_g.studentId, inner_t.timestamp
        ) future
        ON
            future.studentId = s.studentId
        AND
            future.timestamp = t.timestamp
        WHERE
            past.avg < 2.5
        ORDER BY
            t.timestamp, s.studentId;
    """
    ref_df = temporal_converter.conn.sql(sql_query).df()
    ref_time_col = "timestamp"

    print(res_df)
    print(ref_df)

    pd.testing.assert_frame_equal(res_df, ref_df)
    assert res_fkey_col_to_pkey_table is None
    assert res_pkey_col is None
    assert res_time_col == ref_time_col


@pytest.mark.parametrize("pql_log_op, sql_log_op", [
    ("AND", "AND"),
    ("OR", "OR")
])
def test_common_nested_where_tmp(temporal_converter,
                                 pql_log_op,
                                 sql_log_op):
    pql_query = f"""
        PREDICT AVG(grades.grade, 10, 15, DAYS)
        FOR EACH students.studentId
        WHERE AVG(grades.grade, 0, 5, DAYS) < 2.5 {pql_log_op} AVG(grades.grade, 5, 10, DAYS) < 5;
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
            future.avg  AS label
        FROM
            students s
        CROSS JOIN
            timestamp_df t
        LEFT JOIN (
            SELECT
                inner_g.studentId,
                inner_t.timestamp,
                AVG(inner_g.grade) as avg
            FROM
                grades inner_g,
                timestamp_df inner_t
            WHERE
                inner_g.date >= inner_t.timestamp + INTERVAL '0 DAY'
            AND
                inner_g.date < inner_t.timestamp + INTERVAL '5 DAY'
            GROUP BY
                inner_g.studentId, inner_t.timestamp
        ) past1
        ON
            past1.studentId = s.studentId
        AND
            past1.timestamp = t.timestamp
        LEFT JOIN (
            SELECT
                inner_g.studentId,
                inner_t.timestamp,
                AVG(inner_g.grade) as avg
            FROM
                grades inner_g,
                timestamp_df inner_t
            WHERE
                inner_g.date >= inner_t.timestamp + INTERVAL '5 DAY'
            AND
                inner_g.date < inner_t.timestamp + INTERVAL '10 DAY'
            GROUP BY
                inner_g.studentId, inner_t.timestamp
        ) past2
        ON
            past2.studentId = s.studentId
        AND
            past2.timestamp = t.timestamp
        LEFT JOIN (
            SELECT
                inner_g.studentId,
                inner_t.timestamp,
                AVG(inner_g.grade) as avg
            FROM
                grades inner_g,
                timestamp_df inner_t
            WHERE
                inner_g.date >= inner_t.timestamp + INTERVAL '10 DAY'
            AND
                inner_g.date < inner_t.timestamp + INTERVAL '15 DAY'
            GROUP BY
                inner_g.studentId, inner_t.timestamp
        ) future
        ON
            future.studentId = s.studentId
        AND
            future.timestamp = t.timestamp
        WHERE
            past1.avg < 2.5 {sql_log_op} past2.avg < 5
        ORDER BY
            t.timestamp, s.studentId;
    """
    ref_df = temporal_converter.conn.sql(sql_query).df()
    ref_time_col = "timestamp"

    print(res_df)
    print(ref_df)

    pd.testing.assert_frame_equal(res_df, ref_df)
    assert res_fkey_col_to_pkey_table is None
    assert res_pkey_col is None
    assert res_time_col == ref_time_col


@pytest.mark.parametrize("pql_log_op, sql_log_op", [
    ("AND", "AND"),
    ("OR", "OR")
])
def test_stat_pl_common_nested_where_tmp(temporal_converter,
                                         pql_log_op,
                                         sql_log_op):
    pql_query = f"""
        PREDICT AVG(grades.grade WHERE studyInf.favSubject CONTAINS "S", 10, 15, DAYS)
        FOR EACH students.studentId
        WHERE AVG(grades.grade, 0, 5, DAYS) < 2.5 {pql_log_op} AVG(grades.grade, 5, 10, DAYS) < 5;
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
            future.avg  AS label
        FROM
            students s
        CROSS JOIN
            timestamp_df t
        LEFT JOIN (
            SELECT
                inner_g.studentId,
                inner_t.timestamp,
                AVG(inner_g.grade) as avg
            FROM
                grades inner_g,
                timestamp_df inner_t
            WHERE
                inner_g.date >= inner_t.timestamp + INTERVAL '0 DAY'
            AND
                inner_g.date < inner_t.timestamp + INTERVAL '5 DAY'
            GROUP BY
                inner_g.studentId, inner_t.timestamp
        ) past1
        ON
            past1.studentId = s.studentId
        AND
            past1.timestamp = t.timestamp
        LEFT JOIN (
            SELECT
                inner_g.studentId,
                inner_t.timestamp,
                AVG(inner_g.grade) as avg
            FROM
                grades inner_g,
                timestamp_df inner_t
            WHERE
                inner_g.date >= inner_t.timestamp + INTERVAL '5 DAY'
            AND
                inner_g.date < inner_t.timestamp + INTERVAL '10 DAY'
            GROUP BY
                inner_g.studentId, inner_t.timestamp
        ) past2
        ON
            past2.studentId = s.studentId
        AND
            past2.timestamp = t.timestamp
        LEFT JOIN (
            SELECT
                inner_g.studentId,
                inner_t.timestamp,
                AVG(inner_g.grade) as avg
            FROM
                grades inner_g,
                timestamp_df inner_t
            WHERE
                inner_g.date >= inner_t.timestamp + INTERVAL '10 DAY'
            AND
                inner_g.date < inner_t.timestamp + INTERVAL '15 DAY'
            GROUP BY
                inner_g.studentId, inner_t.timestamp
        ) future
        ON
            future.studentId = s.studentId
        AND
            future.timestamp = t.timestamp
        JOIN
            studyInf si
        ON
            si.studentId = s.studentId
        AND
            si.favSubject LIKE '%S%'
        WHERE
            past1.avg < 2.5 {sql_log_op} past2.avg < 5
        ORDER BY
            t.timestamp, s.studentId;
    """
    ref_df = temporal_converter.conn.sql(sql_query).df()
    ref_time_col = "timestamp"

    print(res_df)
    print(ref_df)

    pd.testing.assert_frame_equal(res_df, ref_df)
    assert res_fkey_col_to_pkey_table is None
    assert res_pkey_col is None
    assert res_time_col == ref_time_col
