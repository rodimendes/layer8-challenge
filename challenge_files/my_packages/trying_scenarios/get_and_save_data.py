from get_data import get_file_as_str, get_file_as_dataframe, to_pickle

source = "https://raw.githubusercontent.com/coskunfurkan/kickStarter/master/ks-projects-201801.csv"

# Getting file as text...
my_file = get_file_as_str(source)
# and printing.
print(my_file)

# Getting file as dataframe...
my_file = get_file_as_dataframe(source)
# and saving as a pickle file.
to_pickle(my_file, my_pickle_file_name="my_df")
# Check a new file called my_df.pkl on your folder.
