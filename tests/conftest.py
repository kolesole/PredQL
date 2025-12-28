"""Pytest fixtures and configuration for PredQL tests."""

import numpy as np
import pandas as pd
import pytest
from relbench.base import Database, Table

from predql.converter import SConverterPredQL, TConverterPredQL


@pytest.fixture(scope="session")
def test_db():
    SEED = 42
    N = 10
    REPS = 5
    M = REPS*N
    NONE_PROB = 0.2

    rng = np.random.default_rng(SEED)

    student_id = np.arange(N)
    name = ["oleksii", "jakub", "karel", "mark", "k",
            "anna", "alex", "maryna", "tomas", "michal"]
    students_df = pd.DataFrame({"studentId" : student_id,
                                "name"      : name,})

    students_table = Table(
        df=students_df,
        fkey_col_to_pkey_table=None,
        pkey_col="studentId",
        time_col=None)

    study_year = rng.integers(low=1, high=5, size=N, endpoint=True)
    study_year = study_year.astype(float)
    study_year[rng.random(N) < NONE_PROB] = np.nan
    fav_subject = ["LAG", "LGR", "PST", "SSU", "OPT", np.nan, "MAS", "S", np.nan, "KAT"]
    study_inf_df = pd.DataFrame({"studentId" : student_id,
                                 "year"      : study_year,
                                 "favSubject": fav_subject})

    study_inf_table = Table(
        df=study_inf_df,
        fkey_col_to_pkey_table={"studentId" : "students"},
        pkey_col="studentId",
        time_col=None)

    grade_id = np.arange(M)
    gr_student_id = np.tile(student_id, REPS)
    gr_name = np.tile(name, REPS)
    grade = rng.integers(low=1, high=5, size=M, endpoint=True)
    date = pd.to_datetime("2025-01-01") + pd.to_timedelta(rng.integers(0, 30, size=M), unit="D")
    grade = grade.astype(float)
    grade[rng.random(M) < NONE_PROB] = np.nan

    grades_df = pd.DataFrame({
        "gradeId"   : grade_id,
        "studentId" : gr_student_id,
        "name"      : gr_name,
        "grade"     : grade,
        "date"      : date})

    grades_table = Table(
        df=grades_df,
        fkey_col_to_pkey_table={"studentId" : "students"},
        pkey_col="gradeId",
        time_col="date")

    # print(students_table)
    # print(grades_table)

    table_dict = {
        "students" : students_table,
        "grades"   : grades_table,
        "studyInf" : study_inf_table}

    db = Database(table_dict=table_dict)
    return db

@pytest.fixture(scope="session")
def temporal_converter(test_db):
    timestamps = pd.to_datetime(["2025-01-01", "2025-01-15"])
    timestamps = pd.Series(timestamps)

    return TConverterPredQL(db=test_db, timestamps=timestamps)

@pytest.fixture(scope="session")
def static_converter(test_db):
    return SConverterPredQL(db=test_db)
