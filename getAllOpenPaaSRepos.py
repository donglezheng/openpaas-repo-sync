#!/usr/bin/python
# coding=utf-8
import json
import urllib2
import subprocess

USER='openpaas-ng'

if __name__ == '__main__':
    print("Checking repos\n")
    url = "https://api.github.com/users/{}/repos".format(USER)
    req = urllib2.urlopen(url)
    res = json.load(req)
    for repo in res:
        if not repo['fork']: continue
        cloneCmd = ['git', 'clone', 'https://github.com/' + repo['full_name']] 
        print(cloneCmd)
        subprocess.call(cloneCmd)
        print("")
    #parent_url = res['parent']['git_url']
