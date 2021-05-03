#!/usr/bin/python3
"""Initial file for messing with API's"""
import requests
import sys
import urllib


if __name__ == "__main__":
    baseurl = "https://jsonplaceholder.typicode.com"
    todos = "https://jsonplaceholder.typicode.com/todos"
    t_done = 0
    t_tot = 0
    t_d_list = []
    u_id = sys.argv[1]
    u_url = baseurl + "/users/" + str(u_id)
    r = requests.get(u_url)
    rj = r.json()
    todos_r = requests.get(todos)
    todos_dict = todos_r.json()
    name = rj.get('name')
    for todo in todos_dict:
        if todo.get('userId') == int(u_id):
            t_tot += 1
            if todo.get('completed') is True:
                t_done += 1
                t_d_list.append(todo.get('title'))
    print("Employee {} is done with tasks({}/{}):".format(
        name, t_done, t_tot))
    for task in t_d_list:
        print("\t {}".format(task))
