import pandas as pd
import matplotlib.pyplot as plt 
from colorama import Fore, Style, init
from pprint import pprint


def plot(data,graph_type:str,Title:str):
    plt.figure(figsize=(12, 8))
    data.plot(kind=f'{graph_type}', color='skyblue')
    plt.title(f'{Title}')
    plt.xlabel('Values')
    plt.ylabel('Count')
    plt.xticks(rotation=45)
    plt.show()


def clean_df(df: pd.DataFrame) -> pd.DataFrame:
    df['date'] = df['timestamp'].str.split('T', expand=True)[0]
    df['time'] = df['timestamp'].str.split('T', expand=True)[1].str.split('-', expand=True)[0]
    df['timestamp'] = pd.to_datetime(df['date']+' '+df['time'])
    df['hour'] = df['timestamp'].dt.hour
    return df


def transform_and_rename_dataframe(
    dataframe: pd.DataFrame,
    id_map_dataframe: pd.DataFrame,
    merge_on: str,
    drop_columns: list[str],
    rename_columns: dict[str]
) -> pd.DataFrame:
    """
    Transform and rename a DataFrame by merging it with another DataFrame, dropping specified columns,
    and renaming columns.

    Args:
    - dataframe (pd.DataFrame): The input DataFrame.
    - id_map_dataframe (pd.DataFrame): The DataFrame to merge with.
    - merge_on (str): The column on which to perform the merge.
    - drop_columns (list): List of column names to drop.
    - rename_columns (dict): Dictionary to rename columns.

    Returns:
    - pd.DataFrame: The transformed and renamed DataFrame.
    """
    transformed_dataframe = dataframe.merge(id_map_dataframe, on=merge_on, how='left')
    transformed_dataframe = transformed_dataframe.drop(columns=drop_columns)
    transformed_dataframe = transformed_dataframe.rename(columns=rename_columns)

    return transformed_dataframe
def CPrint(text: str, colour=Fore.BLUE, style=Style.BRIGHT):
    print(style+colour+text+Style.RESET_ALL)