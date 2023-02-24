from thefuzz import fuzz
from thefuzz import process


def find_projects(projects: list, my_search: str, proj_amount: int):
    """
    Helps the user to find a project with indicated word(s).
    """
    print(f"Looking for projects with the word(s): {my_search}")
    return process.extract(my_search, choices=projects, limit=proj_amount)
