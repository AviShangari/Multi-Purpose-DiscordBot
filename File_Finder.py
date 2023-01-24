import os
import json


def find_file(_name):
    for root, dirs, files in os.walk(r"C:\\"):
        if _name in files:
            return os.path.join(root, _name)


def read():
    with open("discord_app_paths.json") as json_file:
        data = json.load(json_file)
        return data


if __name__ == "__main__":

    to_find = input("Which file do you want to add? -----> ")
    path = find_file(to_find)
    temp = read()
    name = input("What would you like to call this application? -----> ")
    temp[name] = path

    f = open("discord_app_paths.json", "w")
    json.dump(temp, f)
    f.close()




