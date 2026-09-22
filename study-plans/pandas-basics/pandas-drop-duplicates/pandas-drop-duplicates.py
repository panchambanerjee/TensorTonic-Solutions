import pandas as pd

def drop_duplicates(data: dict) -> list:
    """
    Returns [rows_before, rows_after, cleaned_data], with integer counts and a dictionary of lists.
    """
    df = pd.DataFrame(data)
    count_dup = len(df)
    df.drop_duplicates(keep='first', inplace=True)
    count_dedup = len(df)
    dedup_df_dict = df.to_dict("list")

    return [
        count_dup, count_dedup, dedup_df_dict
]
