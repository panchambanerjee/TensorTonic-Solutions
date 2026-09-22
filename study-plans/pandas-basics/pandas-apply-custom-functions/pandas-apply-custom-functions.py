import pandas as pd

def apply_transform(data: dict, column: str, operation: str) -> dict:
    """
    Returns the original column lists plus the target column with a _transformed suffix.
    """

    df = pd.DataFrame(data)

    if operation == "normalize":
        min_val = df[column].min()
        max_val = df[column].max()
        df[column + "_transformed"] = df[column].apply(\
            lambda x: round(((x-min_val)/(max_val - min_val)), 4))

    elif operation == "rank":
        df[column + "_transformed"] = df[column].rank().astype(int)

    elif operation == "cumsum":
        df[column + "_transformed"] = df[column].cumsum()

    elif operation == "double":
        df[column + "_transformed"] = df[column].apply(lambda x: 2*x)

    return df.to_dict("list")
