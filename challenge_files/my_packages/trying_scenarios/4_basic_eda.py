from get_data import opening_pickle
from eda import event_occurences, date_occurrences

print("### Opening a previous saved cleaned_data.pkl file.")
cleaned_data = opening_pickle("cleaned_data")

print("### Displaying a graph of an occurrence for exploratory analysis.")
event_occurences(cleaned_data)

print("### And displying a graph for a date event for exploratory analysis.")
date_occurrences(cleaned_data)
