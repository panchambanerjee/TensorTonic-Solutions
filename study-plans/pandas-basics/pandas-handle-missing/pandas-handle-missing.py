import pandas as pd

def handle_missing(data: dict, fill_value: float) -> dict:
    """
    Returns null_counts as a dictionary of integers and cleaned_data as a dictionary of lists.
    """

    df = pd.DataFrame(data)
    
    null_counts = {k:int(v) for k, v in df.isnull().sum().items()}
    df.fillna(fill_value, inplace=True)

    return {
        "null_counts": null_counts,
        "cleaned_data": df.to_dict("list")
    }