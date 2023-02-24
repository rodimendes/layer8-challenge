from find_project import find_projects
from get_data import opening_pickle

print("### It's time to find some project to help.")
print("### Let's search for 3 projects with some word similar to 'lisbon'.")
cleaned_data = opening_pickle("my_df")
words_to_search = input("Tell me a word to find a project: ")
occur = int(input("How many projects to find? "))
print(find_projects(cleaned_data["name"], words_to_search, occur))
