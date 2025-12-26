import pytest
import pandas as pd

# @pytest.mark.parametrize("pql_aggr, sql_aggr", [
#     ("AVG", "AVG"),
#     ("MAX", "MAX"),
#     ("MIN", "MIN"),
#     ("SUM", "SUM")
# ])
@pytest.mark.parametrize("pql_cond, sql_cond", [
    ("!=", "!="),
    ("<", "<"),
    ("<=", "<="),
    ("==", "="),
    (">", ">"),
    (">=", ">=")
])
def test_num_cond_tmp(temporal_converter,
                      pql_cond,
                      sql_cond):
    pql_query = f"""
        PREDICT AVG(grades.grade, 0, 10, DAYS) {pql_cond} 2.5 
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
            CASE
                WHEN AVG(g.grade) {sql_cond} 2.5 THEN true
                ELSE false
            END AS label
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

    pd.testing.assert_frame_equal(res_df, ref_df)
    assert res_fkey_col_to_pkey_table == None
    assert res_pkey_col == None
    assert res_time_col == ref_time_col

# NOTE: DOESN'T WORK WITHOUT STATIC WHERE
@pytest.mark.parametrize("pql_cond, sql_cond", [
    ("CONTAINS", lambda s : f"LIKE '%{s}%'"),
    ("NOT CONTAINS", lambda s : f"NOT LIKE '%{s}%'"),
    ("LIKE", lambda s : f"LIKE '{s}'"),
    ("NOT LIKE", lambda s : f"NOT LIKE '{s}'"),
    ("STARTS WITH", lambda s : f"LIKE '{s}%'"),
    ("ENDS WITH", lambda s : f"LIKE '%{s}'"),
    ("=", lambda s : f"= '{s}'")
])
def test_str_cond_tmp(temporal_converter,
                      pql_cond,
                      sql_cond):
    pql_query = f"""
        PREDICT AVG(grades.grade WHERE students.name {pql_cond} "k", 0, 10, DAYS)
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
        WHERE
            s.name {sql_cond("k")}
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
    assert res_fkey_col_to_pkey_table == None
    assert res_pkey_col == None
    assert res_time_col == ref_time_col
    
#TODO: FIX PROBLEM WITH <<IS NULL>>
@pytest.mark.parametrize("pql_cond, sql_cond", [
    ("IS NOT NULL", "IS NOT NULL"),
    ("IS NULL", "IS NULL")
])
def test_null_cond_tmp(temporal_converter,
                       pql_cond,
                       sql_cond):
    pql_query = f"""
        PREDICT FIRST(grades.grade, 0, 10, DAYS) {pql_cond}
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
            CASE
                WHEN ARRAY_AGG(g.grade ORDER BY g.date)[1] {sql_cond} 
                THEN true
                ELSE false
            END AS label
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
    print(ref_df)
    print(res_df)

    pd.testing.assert_frame_equal(res_df, ref_df)
    assert res_fkey_col_to_pkey_table == None
    assert res_pkey_col == None
    assert res_time_col == ref_time_col
    