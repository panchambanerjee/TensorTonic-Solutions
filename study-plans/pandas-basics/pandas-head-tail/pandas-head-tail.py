import pandas as pd

def head_tail(data: dict, n: int) -> dict:
    """
    Returns head and tail as dictionaries mapping columns to value lists.
    """
    
    df = pd.DataFrame(data)
    head_col_dict = df.head(n).to_dict("list")
    bot_col_dict = df.tail(n).to_dict("list")

    return {
        "head": head_col_dict,
        "tail": bot_col_dict
    }