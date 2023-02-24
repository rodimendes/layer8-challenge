from get_data import opening_pickle
from data_cleaning import get_auto_profile

# Opening a previous saved my_df.pkl file...
my_pickle_file = opening_pickle("my_df")
# and printing columns names and first row
print(my_pickle_file.columns)
print(my_pickle_file.head(1))

# Generating auto report
get_auto_profile(my_pickle_file, report_name="my_first_report")
# Check a new html file called my_first_report.html
