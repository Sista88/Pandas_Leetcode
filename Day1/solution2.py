import pandas as pd


def getDataframeSize(players: pd.DataFrame) -> List[int]:
    df = players.shape
    return list(df)
