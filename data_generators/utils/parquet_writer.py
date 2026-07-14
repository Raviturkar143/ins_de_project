import os


def write_parquet(df, output_path):

    """
    Writes dataframe into parquet format.

    Parameters:
        df          : pandas DataFrame
        output_path : target directory path
    """

    os.makedirs(
        output_path,
        exist_ok=True
    )

    file_path = os.path.join(
        output_path,
        "part-000.parquet"
    )

    df.to_parquet(
        file_path,
        engine="pyarrow",
        index=False
    )

    print(
        f"Parquet created successfully: {file_path}"
    )