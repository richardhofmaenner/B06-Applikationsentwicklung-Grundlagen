#!/usr/bin/env python3
# coding: utf8

import json
import os.path
from datetime import datetime

def load_last_logins(json_file_name):
    result = dict()
    if os.path.exists(json_file_name):
        with open(json_file_name, "r") as f:
            result = json.load(f)
    return result

def main():
    json_file_name = "Tag02/Übungen/all_logins.json"
    all_logins = load_last_logins(json_file_name)

    user_name = input("Please enter you name: ")

    last_login = "<never>"
    current_time = datetime.now().strftime("%d. %b. %Y %H:%M:%S")


    # check if the login ever has been used
    if len(all_logins) > 0:
        # iterate over all logins and assign the last login if the user has logged in before.
        # otherwise the default value "<never>" is used
        for key, value in all_logins.items():
            if key == user_name:
                last_login = value
                break
            else:
                last_login = "<never>"

    print(f"Hello {user_name}\nyour last login was {last_login}.\nNow is {current_time}")

    # add the current login to the dictionary
    all_logins[user_name] = current_time
    
    # write the dictionary to the json file
    with open(json_file_name, "w") as f:
        json.dump(all_logins, f)


if __name__ == '__main__':
    main()