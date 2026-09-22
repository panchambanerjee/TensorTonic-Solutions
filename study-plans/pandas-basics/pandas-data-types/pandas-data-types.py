import pandas as pd

def data_types_overview(data: dict) -> dict:
    """
    Returns a dictionary with dtypes, type_counts, and num_columns.
    """
    df = pd.DataFrame.from_dict(data)

    output_dict = {
        "num_columns": len(df.columns),
        "dtypes": df.dtypes.astype(str).to_dict(),
        "type_counts": df.dtypes.astype(str).value_counts().to_dict()
    }

    return output_dict