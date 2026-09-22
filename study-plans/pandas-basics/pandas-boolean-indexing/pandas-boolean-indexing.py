import pandas as pd

def boolean_filter(data: dict, column: str, threshold: float) -> dict:
    """
    Returns filtered_data as a dictionary of lists and count as an integer.
    """
    df = pd.DataFrame(data)

    filtered_data = df[df[column]>threshold]

    output_dict = {
        "filtered_data": filtered_data.to_dict("list"),
        "count": len(filtered_data)
    }

    return output_dict