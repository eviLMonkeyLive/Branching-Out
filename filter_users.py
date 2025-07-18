"""
filter_users.py

This module provides functions to filter user data based on different criteria.

Currently included:
- filter_users_by_name(name): Prints users matching the specified name.
- filter_by_age(age): Prints users matching the specified age.

Usage:
    Import this module and call the filtering functions with appropriate arguments.

Example:
    from filter_users import filter_users_by_name

    matched_users = filter_users_by_name("Alice")
"""
import json


def filter_users_by_name(name):
    """
    Filters and prints users that match the given name.

    Args:
        name (str): The name to filter users by.
    """
    with open("users.json", "r") as file:
        users = json.load(file)

    filtered_users = [user for user in users if user["name"].lower() == name.lower()]

    for user in filtered_users:
        print(user)


def filter_by_age(age):
    """
    Filters and prints users that match the given age.

    Args:
        age (int): The age to filter users by.
    """
    with open("users.json", "r") as file:
        users = json.load(file)

    filtered_users = [user for user in users if user["age"] == age]

    for user in filtered_users:
        print(user)


def filter_by_email(email):
    """
    Filters and prints users that match the given email.

    Args:
        email (str): The email to filter users by.
    """
    with open("users.json", "r") as file:
        users = json.load(file)

    filtered_users = [user for user in users if user["email"].lower() == email.lower()]

    for user in filtered_users:
        print(user)


if __name__ == "__main__":
    filter_option = input("What would you like to filter by? (Currently, only 'name', 'age' and 'email' are supported): ").strip().lower()

    if filter_option == "name":
        name_to_search = input("Enter a name to filter users: ").strip()
        filter_users_by_name(name_to_search)
    elif filter_option == "age":
        age_to_search = input("Enter an age to filter users: ").strip()
        filter_by_age(int(age_to_search))
    elif filter_option == "email":
        email_to_search = input("Enter an email to filter users: ").strip()
        filter_by_email(email_to_search)
    else:
        print("Filtering by that option is not yet supported.")
