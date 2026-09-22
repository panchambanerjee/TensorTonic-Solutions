import pandas as pd

def iloc_selection(data: dict, row: int, col: int) -> list:
    """
    Returns [element, row_values, col_values], with both value sequences as lists.
    """
    df = pd.DataFrame(data)
    el_1 = df.iloc[row, col]
    el_row = df.iloc[row, :].tolist()
    el_col = df.iloc[:, col].tolist()

    return [el_1, el_row, el_col]
