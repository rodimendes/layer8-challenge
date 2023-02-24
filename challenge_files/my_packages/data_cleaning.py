import pandas as pd
from ydata_profiling import ProfileReport
from get_data import get_file_as_dataframe
from sklearn.preprocessing import LabelEncoder

pd.options.display.float_format = '{:,.2f}'.format


def get_auto_profile(file, report_name: str = "my_report"):
    """
    Create automatic report in **.html** format
    """
    print("Your report is in development... Please, wait.")
    auto_profile = ProfileReport(file, title="Auto Report")
    auto_profile.to_file(f"{report_name}.html")


def head(file):
    """
    Returns the head.
    """
    return file.head()


def df_size(file):
    """
    Returns the dataframe size.
    """
    return f"The dataset has {file.shape[0]} rows and {file.shape[1]} columns."


def describe(file):
    """
    Returns the description of the data.
    """
    return file.describe()


def cleaning_missing_data(file):
    """
    Deals with missing data.
    """
    print(f"The dataset had {file.shape[0]} rows and {file.shape[1]} columns.")
    raw_data = file.dropna(subset=['name', 'usd pledged']).reset_index(drop=True)
    raw_data.isna().sum()
    print(f"Now, the dataset has {raw_data.shape[0]} rows and {raw_data.shape[1]} columns.")
    print(f"It was reduced in {(100 - (raw_data.shape[0] / file.shape[0] * 100)):.2f}%")
    return raw_data


def dropping_duplicated_rows(file):
    """
    Deals with duplicated data.
    """
    return file.drop_duplicates()


def label_encoding(file):
    """
    Encodes the target variable.
    """
    label_encoder = LabelEncoder()
    target = file['state']
    label_encoder.fit(target)
    encoded_target = label_encoder.transform(target)
    file['encoded_state'] = encoded_target
    file['real_state'] = file['state']
    file = file.drop(labels='state', axis=1)
    return file


def full_preprocessing(file):
    """
    Executes all preprocessing steps and returns a cleaned dataset.
    """
    print("Treating missing values")
    missing = cleaning_missing_data(file)
    print("Solving duplicate entries")
    duplicated = dropping_duplicated_rows(missing)
    print("Labeling features")
    clean_df = label_encoding(duplicated)
    print("Process finished")
    return clean_df
