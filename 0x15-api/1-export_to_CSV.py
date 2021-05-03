#!/usr/bin/python3
"""Initial file for messing with API's"""
import csv
import requests
import sys


if __name__ == "__main__":
    baseurl = "https://jsonplaceholder.typicode.com"
    todos = "https://jsonplaceholder.typicode.com/todos"
    t_dict = {}
    u_id = sys.argv[1]
    u_url = baseurl + "/users/" + str(u_id)
    r = requests.get(u_url)
    rj = r.json()
    todos_r = requests.get(todos)
    todos_dict = todos_r.json()
    name = rj.get('username')
    filename = str(u_id) + ".csv"
    with open(filename, 'w') as file:
        writer = csv.writer(file, quoting=csv.QUOTE_ALL)
        for todo in todos_dict:
            if todo.get('userId') == int(u_id):
                c = todo.get('completed')
                t = todo.get('title')
                writer.writerow([u_id, name, c, t])
