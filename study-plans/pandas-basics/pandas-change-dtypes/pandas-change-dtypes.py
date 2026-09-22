import pandas as pd

def change_dtype(data: dict, column: str, target_type: str) -> list:
    """
    Returns [dtypes_before, dtypes_after], both dictionaries of column names to dtype strings.
    """
    
    df = pd.DataFrame(data)

    df_pre_dtypes = df.dtypes.astype(str).to_dict()

    df[column] = df[column].astype(target_type)

    df_post_dtypes = df.dtypes.astype(str).to_dict()

    return [df_pre_dtypes, df_post_dtypes]