import pandas as pd


def pivotTable(weather: pd.DataFrame) -> pd.DataFrame:
    df = pd.pivot_table(weather, values="temperature", columns="city", index="month")
    return df
