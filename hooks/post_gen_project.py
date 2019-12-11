#!/usr/bin/env python
import http.client
import os
import platform
import urllib.parse

PROJECT_DIRECTORY = os.path.realpath(os.path.curdir)


def remove_file(filepath):
    os.remove(os.path.join(PROJECT_DIRECTORY, filepath))

def post_ga_data():
    params = urllib.parse.urlencode({
        'v': 1,
        'tid': 'UA-136298016-1',
        'uid': '{{ cookiecutter.email }}',
        't' : 'event',
        'ec': 'carol_cookiecuter',
        'ea': 'new_online_project',
        'el': 'carol_online_app',
        'cd1': 'carol_environment',
        'cm1': '{{ cookiecutter.carol_app_organization }}',
        'cd2': 'project',
        'cm2': '{{ cookiecutter.project_name }}',
        'cd3': 'os',
        'cm3': platform.system(),
        'cd4': 'python_version',
        'cm4': platform.python_version(),
        'cd5': 'carol_organization',
        'cm5': '{{ cookiecutter.carol_app_environment }}'
    })

    try:
        connection = http.client.HTTPConnection('www.google-analytics.com')
        connection.request('POST', '/collect', params)
    except Exception as e:
        print(e)

post_ga_data()

if __name__ == '__main__':
    pass
