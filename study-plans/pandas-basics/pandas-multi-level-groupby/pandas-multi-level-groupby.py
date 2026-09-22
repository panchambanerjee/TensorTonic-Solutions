import pandas as pd

def multi_groupby(data: dict, group_cols: list, value_col: str, aggfunc: str) -> dict:
    """
    Returns a dictionary of lists for the grouping columns and aggregated value column.
    """
    df = pd.DataFrame(data)

    grouped = df.groupby(group_cols)[value_col].agg(aggfunc).reset_index()

    return grouped.to_dict("list")
