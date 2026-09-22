import pandas as pd

def select_columns(data: dict, columns: list) -> dict:
    """
    Returns a dictionary of value lists in the requested column order.
    """

    df_filtered = pd.DataFrame(data)[columns]
    return df_filtered.to_dict("list")
    
