import pandas as pd

def set_index_column(data: dict, index_col: str) -> dict:
    """
    Returns index_values and columns as lists, plus data as a dictionary of lists.
    """
    df = pd.DataFrame(data)

    index_values = df[index_col].values
    
    df.drop(index_col, axis=1, inplace=True)
    col_list = df.columns.tolist()
    data_remaining = df.to_dict("list")

    return {
        "index_values": index_values.tolist(),
        "columns": col_list,
        "data": data_remaining
    }
