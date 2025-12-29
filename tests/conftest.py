import numpy as np
import pandas as pd
import pytest
from relbench.base import Database, Table

from predql.converter import SConverterPredQL, TConverterPredQL

from io import StringIO

@pytest.fixture(scope="session")
def test_db():
    students_data = """
    studentId, name
    0,         oleksii
    1,         jakub
    2,         karel
    """
    students_df = pd.read_csv(StringIO(students_data), 
                              skipinitialspace=True,
                              na_values=['nan', 'NaN', 'NONE', ''])
    students_table = Table(
        df=students_df,
        fkey_col_to_pkey_table=None,
        pkey_col="studentId",
        time_col=None)

    fav_subjects_data = """
    studentId, subject,    date
    0,         OPT,        2025-01-01
    0,         ALG,        2025-01-10
    1,         PRP,        2025-01-01
    1,         P,          2025-01-10
    2,         nan,        2025-01-01
    """
    fav_subjects_df = pd.read_csv(StringIO(fav_subjects_data), 
                               skipinitialspace=True,
                               parse_dates=["date"],
                               na_values=['nan', 'NaN', 'NONE', ''])
    fav_subjects_table = Table(
        df=fav_subjects_df,
        fkey_col_to_pkey_table={"studentId" : "students"},
        pkey_col=None,
        time_col="date")
    
    study_inf_data = """
    studentId, studyYear, mainInterest
    0,         3,         AI
    1,         7,         DS
    2,         nan,       SI
    """
    study_inf_df = pd.read_csv(StringIO(study_inf_data), 
                               skipinitialspace=True,
                               na_values=['nan', 'NaN', 'NONE', ''])
    study_inf_table = Table(
        df=study_inf_df,
        fkey_col_to_pkey_table={"studentId" : "students"},
        pkey_col=None,
        time_col=None)

    grades_data = """
    gradeId, studentId, grade, date
    0,       0,         1,     2025-01-01
    1,       0,         1,     2025-01-04
    2,       0,         2,     2025-01-05
    3,       0,         2,     2025-01-06
    4,       0,         2,     2025-01-07
    5,       0,         nan,   2025-01-08
    6,       0,         4,     2025-01-15
    7,       1,         2,     2025-01-04
    8,       1,         1,     2025-01-14
    9,       1,         1,     2025-01-15
    10,      1,         4,     2025-01-19
    11,      2,         nan,   2025-01-03
    """
    grades_df = pd.read_csv(StringIO(grades_data), 
                            skipinitialspace=True, 
                            parse_dates=["date"],
                            na_values=['nan', 'NaN', 'NONE', ''])
    grades_table = Table(
        df=grades_df,
        fkey_col_to_pkey_table={"studentId" : "students"},
        pkey_col="gradeId",
        time_col="date")

    table_dict = {
        "students"    : students_table,
        "favSubjects" : fav_subjects_table,
        "studyInf"    : study_inf_table,
        "grades"      : grades_table}

    db = Database(table_dict=table_dict)
    return db

@pytest.fixture(scope="session")
def temporal_converter(test_db):
    timestamps = pd.to_datetime(["2025-01-01", "2025-01-10"])
    timestamps = pd.Series(timestamps)

    return TConverterPredQL(db=test_db, timestamps=timestamps)

@pytest.fixture(scope="session")
def static_converter(test_db):
    return SConverterPredQL(db=test_db)
