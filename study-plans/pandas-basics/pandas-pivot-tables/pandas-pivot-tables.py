import pandas as pd

def create_pivot(data: dict, index: str, columns: str, values: str, aggfunc: str) -> dict:
    """
    Returns a dictionary from column labels to dictionaries of row labels and aggregates.
    """
    df = pd.DataFrame(data)

    pivot = df.pivot_table(index=index, \
                          columns=columns, \
                          values=values,\
                          aggfunc=aggfunc,
                          fill_value=0)
    return pivot.to_dict()
