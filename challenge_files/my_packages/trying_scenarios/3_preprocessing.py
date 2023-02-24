from get_data import opening_pickle, to_pickle
from data_cleaning import describe, df_size, cleaning_missing_data, dropping_duplicated_rows, label_encoding, full_preprocessing

print("### Opening my_df.pkl and...")
my_pickle_file = opening_pickle("my_df")

print("### describing the dataset...")
print(describe(my_pickle_file))

print("### printing dataset size...")
print(df_size(my_pickle_file))

print("### dealing with missing data and printing one random row...")
print(cleaning_missing_data(my_pickle_file).sample(1))

print("### dealing with duplicated data...")
dropping_duplicated_rows(my_pickle_file)

print("### and enconding state column.")
print(label_encoding(my_pickle_file).columns)

print("### Or you can execute the full preprocessing in a row and saving as a pickle file.")
to_pickle(full_preprocessing(my_pickle_file), "cleaned_data")
