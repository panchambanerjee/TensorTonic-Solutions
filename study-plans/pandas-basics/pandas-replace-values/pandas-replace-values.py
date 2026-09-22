import pandas as pd

def replace_values(data: dict, column: str, old_val: object, new_val: object) -> dict:
    """
    Returns data as a dictionary of updated lists and count as an integer.
    """

    df = pd.DataFrame(data)

    counts = int((df[column]==old_val).sum())

    df[column] = df[column].replace(old_val, new_val)

    return {
        "data": df.to_dict("list"),
        "count": counts
    }
