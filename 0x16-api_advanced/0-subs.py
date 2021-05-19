#!/usr/bin/python3
""" This file will be API"""
import requests
import sys


def number_of_subscribers(subreddit):
    """ gets the number of subscribers for the given subreddit"""
    if subreddit is None:
        return 0
    url = "https://www.reddit.com/r/" + str(subreddit) + "/about.json"
    headers = {'User-Agent': 'Sel'}
    r = requests.get(url, headers=headers, allow_redirects=False)
    if r.status_code != 200:
        return 0
    rj = r.json()
    rjd = rj.get('data')
    return rjd.get('subscribers')
