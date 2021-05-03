#!/usr/bin/python3
"""Initial file for messing with API's"""
import json
import requests
import sys


if __name__ == "__main__":
    baseurl = "https://jsonplaceholder.typicode.com"
    todos = "https://jsonplaceholder.typicode.com/todos"
    task_dict = {}
    list_dict = []
    u_id = sys.argv[1]
    u_url = baseurl + "/users/" + str(u_id)
    r = requests.get(u_url)
    rj = r.json()
    todos_r = requests.get(todos)
    todos_dict = todos_r.json()
    name = rj.get('username')
    filename = str(u_id) + ".json"
    for todo in todos_dict:
        if todo.get('userId') == int(u_id):
            x = {
                "task": todo.get('title'),
                "completed": todo.get('completed'),
                "username": name
            }
            list_dict.append(x)
    task_dict[u_id] = list_dict
    json_string = json.dumps(task_dict)
    with open(filename, 'w') as outfile:
        json.dump(task_dict, outfile)
