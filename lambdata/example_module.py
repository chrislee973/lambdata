import numpy as np
import pandas as pd

FAV_NUMS = [1,2,3,4,5]

def null_count(df):
    """Checks the dataframe for nulls and returns the total number of nulls"""

    return df.isnull().sum().sum()

def append_list_df(df, l, col_name): 
    """Takes a list, converts it to Series, and then appends it to Dataframe as a new column named 'col_name' """

    #Turn l to series and add as a new column to df
    df[col_name] = pd.Series(l).values

    return df


