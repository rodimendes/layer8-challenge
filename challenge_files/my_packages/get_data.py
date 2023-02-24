import pickle


def get_file_as_str(filepath):
    """
    Get source file as plain text
    """
    import requests

    raw_file_str = requests.get(filepath)
    return raw_file_str.text


def get_file_as_dataframe(filepath):
    """
    Gets source file and converts to dataframe. We suggest assigning it to a variable and printing just the **head** on the screen to check, avoiding long waiting times in the case of very large files to future uses.
    """
    import pandas as pd

    if filepath[-3:] == "csv":
        raw_file = pd.read_csv(filepath, parse_dates=['deadline', 'launched'])
        raw_df = pd.DataFrame(raw_file)
    elif filepath[-4:] == "xlsx":
        raw_file = pd.read_excel(filepath)
        raw_df = pd.DataFrame(raw_file)
    return raw_df


def to_pickle(data, my_pickle_file_name: str = "my_dataset"):
    """
    Saving picklefile in the same folder
    """

    with open(f"{my_pickle_file_name}.pkl", "wb") as file:
        pickle.dump(data, file)


def opening_pickle(picklefile_name):
    """
    Give pickle file name without **.pkl** extension.
    """

    with open(f"{picklefile_name}.pkl", "rb") as file:
        raw_data = pickle.load(file)
    return raw_data
