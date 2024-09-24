import pandas as pd


def findHeavyAnimals(animals: pd.DataFrame) -> pd.DataFrame:
    df = pd.DataFrame(
        animals.query("weight>100").sort_values(["weight"], ascending=False)["name"]
    )
    return df
