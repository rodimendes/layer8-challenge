from find_project import find_projects
from get_data import opening_pickle

# It's time to find some project to help.
# Let's search for 3 projects with some word similar to 'lisbon'.
cleaned_data = opening_pickle("my_df")
print(find_projects(cleaned_data["name"], "lisbon", 3))
