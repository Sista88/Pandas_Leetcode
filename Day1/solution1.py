import pandas as pd


def createDataframe(student_data: List[List[int]]) -> pd.DataFrame:
    df = pd.DataFrame(student_data)
    df.rename(columns={0: "student_id"}, inplace=True)
    df.rename(columns={1: "age"}, inplace=True)
    return df
