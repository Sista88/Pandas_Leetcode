import pandas as pd


def selectData(students: pd.DataFrame) -> pd.DataFrame:
    df = students.query("student_id == 101")
    return df[["name", "age"]]
