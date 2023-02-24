from get_data import opening_pickle, to_pickle
from data_cleaning import describe, df_size, cleaning_missing_data, dropping_duplicated_rows, label_encoding, full_preprocessing

# Opening my_df.pkl and...
my_pickle_file = opening_pickle("my_df")

# describing the dataset...
print(describe(my_pickle_file))

# printing dataset size...
print(df_size(my_pickle_file))

# dealing with missing data and printing one random row...
print(cleaning_missing_data(my_pickle_file).sample(1))

# dealing with duplicated data...
dropping_duplicated_rows(my_pickle_file)

# and enconding state column.
print(label_encoding(my_pickle_file).columns)

# Or you can execute the full preprocessing in a row and saving as a pickle file.
to_pickle(full_preprocessing(my_pickle_file), "cleaned_data")
