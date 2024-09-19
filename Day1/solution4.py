import pandas as pd


def selectFirstRows(employees: pd.DataFrame) -> pd.DataFrame:
    var = employees.head(3)
    return var
