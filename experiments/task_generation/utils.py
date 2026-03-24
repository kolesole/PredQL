import duckdb
import numpy as np
import pandas as pd

from predql.base import Database, Table
from predql.converter import TConverter

from relbench.datasets import Dataset
from relbench.tasks import BaseTask


def execute_sql_query(db        : Database,
                      sql_query : str) -> Table:
    conn = duckdb.connect()
    for name, table in db.table_dict.items():
        conn.register(name, table.df)

    df = conn.sql(sql_query).df()
    return Table(df=df,
                 fkey_col_to_pkey_table={},
                 pkey_col=None,
                 time_col="timestamp")


def get_timestamps(dataset             : Dataset,
                   timedelta           : pd.Timedelta,
                   num_eval_timestamps : int,
                   split               : str) -> "pd.Series[pd.Timestamp]":
    db = dataset.get_db(upto_test_timestamp=(split != "test"))

    if split == "train":
        start = dataset.val_timestamp - timedelta
        end = db.min_timestamp
        freq = -timedelta
    elif split == "val":
        start = dataset.val_timestamp
        end = min(
            dataset.val_timestamp
            + timedelta * (num_eval_timestamps - 1),
            dataset.test_timestamp - timedelta,
            )
        freq = timedelta
    elif split == "test":
        start = dataset.test_timestamp
        end = min(
            dataset.test_timestamp
            + timedelta * (num_eval_timestamps - 1),
            db.max_timestamp - timedelta,
            )
        freq = timedelta
    else:
        pass

    timestamps = pd.date_range(start=start, end=end, freq=freq)
    return timestamps


def process_df_rb(df_rb     : pd.DataFrame,
                  fk        : str,
                  timestamp : str,
                  label     : str) -> pd.DataFrame:
    renamed_df_rb = df_rb.rename(columns={fk        : 'fk',
                                          timestamp : 'timestamp',
                                          label     : 'label'})
    df_rb = renamed_df_rb.sort_values(by=['timestamp', 'fk'])

    df_rb['timestamp'] = df_rb['timestamp']

    return df_rb


def merge_dataframes(df_rb     : pd.DataFrame,
                     df_predql : pd.DataFrame) -> None:
    def normalize(x):
        if isinstance(x, (list, np.ndarray, tuple)):
            return tuple(sorted(x))
        return x

    df_rb['label'] = df_rb['label'].apply(normalize)
    df_predql['label'] = df_predql['label'].apply(normalize)

    merged = pd.merge(
    df_rb,
    df_predql,
    on=['fk', 'timestamp', 'label'],
    how='outer',
    suffixes=('_rb', '_predql'),
    indicator=True
    )

    print(f"Only in RelBench:\n {merged[merged['_merge'] == 'left_only']}")
    print(f"Only in PredQL:\n {merged[merged['_merge'] == 'right_only']}")
    print(f"In both:\n {merged[merged['_merge'] == 'both']}")


def check_correctness(dataset            : Dataset,
                      task               : BaseTask,
                      split              : str,
                      predql_query       : str,
                      fk_col_name        : str,
                      timestamp_col_name : str,
                      label_col_name     : str,
                      execute            : bool=True) -> None:
    timestamps = get_timestamps(dataset, task.timedelta, task.num_eval_timestamps, split)

    print(f"TIMEDELTA: {task.timedelta}")
    print(f"NUM_EVAL_TIMESTAMPS: {task.num_eval_timestamps}")

    converter = TConverter(dataset.get_db(upto_test_timestamp=(split != "test")), timestamps)
    table_rb = task.get_table(split, mask_input_cols=False)
    df_rb = process_df_rb(table_rb.df, fk_col_name, timestamp_col_name, label_col_name)
    if execute:
        table_predql = converter.convert(predql_query, execute=True)
        df_predql = table_predql.df
    else:
        gen_sql_query = converter.convert(predql_query)
        print(gen_sql_query)
        table_predql = execute_sql_query(converter.db, gen_sql_query)
        df_predql = table_predql.df

    print(f"------------------- START {split.upper()} -------------------")
    print(f"RelBench fkeys: {table_rb.fkey_col_to_pkey_table}")
    print(f"RelBench pkey: {table_rb.pkey_col}")
    print(f"RelBench time col: {table_rb.time_col}")
    print(f"PredQL fkeys: {table_predql.fkey_col_to_pkey_table}")
    print(f"PredQL pkey: {table_predql.pkey_col}")
    print(f"PredQL time col: {table_predql.time_col}")
    merge_dataframes(df_rb, df_predql)
    print(f"------------------- END {split.upper()} ---------------------")
