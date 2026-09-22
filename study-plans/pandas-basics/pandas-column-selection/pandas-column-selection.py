import pandas as pd

def select_column(data: dict, column: str) -> dict:
    """
    Returns a dictionary with values as a list and length as an integer.
    """
    df = pd.DataFrame.from_dict(data)
    

    output_dict = {
        "length": int(len(df[column])),
        "values": [x for x in df[column]]
    }

    return output_dict
