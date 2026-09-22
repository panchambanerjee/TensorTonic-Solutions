import pandas as pd

def concat_dataframes(dfs: list) -> list:
    """
    Returns [shape, data], with shape [rows, columns] and data a dictionary of lists.
    """
    dataframes = [pd.DataFrame(df) for df in dfs]
    df_out = pd.concat(dataframes, ignore_index=True)

    return [list(df_out.shape), df_out.to_dict("list")]
