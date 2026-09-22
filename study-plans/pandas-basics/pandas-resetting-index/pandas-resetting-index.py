import pandas as pd

def reset_index_demo(data: dict, index_col: str) -> list:
    """
    Returns [columns_before_reset, columns_after_reset], both lists of strings.
    """

    df = pd.DataFrame(data)
    
    df = df.set_index(index_col)
    list_1 = df.columns.tolist()

    df.reset_index(inplace=True)
    list_2 = df.columns.tolist()

    return [list_1, list_2]
    