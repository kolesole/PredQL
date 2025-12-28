"""Tests for temporal converter WHERE clause handling."""

from io import StringIO

import pandas as pd
import pytest


# def test_stat_where_tmp(temporal_converter):
#     pql_query = """
#         PREDICT AVG(grades.grade WHERE studyInf.favSubject CONTAINS "S", 0, 10, DAYS)
#         FOR EACH students.studentId;
#     """
#     res_table = temporal_converter.convert(pql_query)
#     res_df = res_table.df()
#     res_fkey_col_to_pkey_table = res_table.fkey_col_to_pkey_table
#     res_pkey_col = res_table.pkey_col
#     res_time_col = res_table.time_col

#     sql_query = """
#         SELECT
#             s.studentId AS fk,
#             t.timestamp AS timestamp,
#             AVG(g.grade) AS label
#         FROM
#             students s
#         CROSS JOIN
#             timestamp_df t
#         LEFT JOIN
#             grades g
#         ON
#             g.studentId = s.studentId
#         AND
#             g.date >= t.timestamp + INTERVAL '0 DAY'
#         AND
#             g.date < t.timestamp + INTERVAL '10 DAY'
#         JOIN
#             studyInf si
#         ON
#             si.studentId = s.studentId
#         AND
#             si.favSubject LIKE '%S%'
#         GROUP BY
#             s.studentId, t.timestamp
#         ORDER BY
#             t.timestamp, s.studentId;
#     """
#     ref_df = temporal_converter.conn.sql(sql_query).df()
#     ref_time_col = "timestamp"

#     print(res_df)
#     print(ref_df)

#     pd.testing.assert_frame_equal(res_df, ref_df)
#     assert res_fkey_col_to_pkey_table is None
#     assert res_pkey_col is None
#     assert res_time_col == ref_time_col


def test_common_simple_where_tmp(temporal_converter):
    pql_query = """
        PREDICT AVG(grades.grade, 0, 10, DAYS)
        FOR EACH students.studentId
        WHERE LAST(grades.grade, 0, 10, DAYS) IS NOT NULL;
    """
    res_table = temporal_converter.convert(pql_query)
    res_df = res_table.df()
    res_fkey_col_to_pkey_table = res_table.fkey_col_to_pkey_table
    res_pkey_col = res_table.pkey_col
    res_time_col = res_table.time_col

    ref_data = """
        fk, timestamp,  label
        1,  2025-01-01, 2.0
        0,  2025-01-10, 4.0
        1,  2025-01-10, 2.0
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


@pytest.mark.parametrize("pql_op", [
    ("AND"),
    ("OR")
])
def test_common_nested_where_tmp(temporal_converter,
                                 pql_op):
    pql_query = f"""
        PREDICT AVG(grades.grade, 0, 10, DAYS)
        FOR EACH students.studentId
        WHERE LAST(grades.grade, 0, 10, DAYS) IS NOT NULL 
        {pql_op} (FIRST(favSubjects.subject, 0, 10, DAYS) IS NULL
        OR FIRST(favSubjects.subject, 0, 10, DAYS) CONTAINS "P");
    """
    res_table = temporal_converter.convert(pql_query)
    res_df = res_table.df()
    res_fkey_col_to_pkey_table = res_table.fkey_col_to_pkey_table
    res_pkey_col = res_table.pkey_col
    res_time_col = res_table.time_col

    match pql_op:
        case "AND":
            ref_data = """
                fk, timestamp,  label
                1,  2025-01-01, 2.0
                1,  2025-01-10, 2.0
            """
        case "OR":
            ref_data = """
                fk, timestamp,  label
                0,  2025-01-01, 1.6
                1,  2025-01-01, 2.0
                2,  2025-01-01, nan
                0,  2025-01-10, 4.0
                1,  2025-01-10, 2.0
                2,  2025-01-10, nan
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