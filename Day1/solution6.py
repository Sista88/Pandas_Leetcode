import pandas as pd


def dropDuplicateEmails(customers: pd.DataFrame) -> pd.DataFrame:
    cus = customers.drop_duplicates(subset="email")
    return cus
