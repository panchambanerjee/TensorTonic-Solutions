import pandas as pd

def groupby_basics(data: dict, group_col: str, value_col: str) -> dict:
    """
    Returns sum, mean, and count dictionaries keyed by group label.
    """

    df = pd.DataFrame(data)
    sum_dict = df.groupby(group_col)[value_col].sum().to_dict()
    mean_dict = df.groupby(group_col)[value_col].mean().to_dict()
    count_dict = df.groupby(group_col)[value_col].count().to_dict()
    
    return {"sum": sum_dict, "mean": mean_dict, "count": count_dict}