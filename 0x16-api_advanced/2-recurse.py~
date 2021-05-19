#!/usr/bin/python3
""" This file will be API"""
import requests
import sys


def top_ten(subreddit):
    """Top ten posts"""
    if subreddit is None:
        print("None")
        return
    url = "https://www.reddit.com/r/" + str(subreddit) + "/top/.json?limit=10"
    headers = {'User-Agent': 'Sel'}
    r = requests.get(url, headers=headers, allow_redirects=False)
    if r.status_code != 200:
        print("None")
        return
    rj = r.json().get('data').get('children')
    for post in rj:
        child_dict = post['data']
        print(child_dict.get('title'))
