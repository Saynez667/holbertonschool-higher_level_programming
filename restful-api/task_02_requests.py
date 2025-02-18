#!/usr/bin/python3
'''module for fetch and print'''
import requests
import csv


def fetch_and_print_posts():
    '''send a requests http get to the url and print status 200'''
    r = requests.get('https://jsonplaceholder.typicode.com/posts')
    print(f"Status Code: {r.status_code}")
    '''if the status code are 200 we convert JSON into a obj in python'''
    if r.status_code == 200:
        posts = r.json()
        '''Scan through each post in the list and print the title of each'''
        for post in posts:
            print(post['title'])


def fetch_and_save_posts():
    '''send a requests get to the url  and print status 200'''
    r = requests.get('https://jsonplaceholder.typicode.com/posts')
    '''if its satus 200 we convert the json to a obj in python'''
    if r.status_code == 200:
        posts = r.json()
        '''Create a new list of dict containing only the id,title,body'''
        posts_data = [
            {'id': post['id'], 'title': post['title'], 'body': post['body']}
            for post in posts
            ]
        with open('posts.csv', 'w', newline='') as file:
            writer = csv.DictWriter(file, fieldnames=['id', 'title', 'body'])
            writer.writeheader()
            writer.writerows(posts_data)


if __name__ == "__main__":
    fetch_and_print_posts()
    fetch_and_save_posts()
