#!/usr/bin/python2.7
# merge two json files, given as command line arguments, and output merged json data

import sys
from pprint import pprint
import json

def merge_recursively(a, b, path=None):
    "merges b into a"
    if path is None: path = []
    for key in b:
        if key in a:
            if isinstance(a[key], dict) and isinstance(b[key], dict):
                merge_recursively(a[key], b[key], path + [str(key)])
            elif a[key] == b[key]:
                pass # same leaf value
            else:
                a[key] = b[key]
        else:
            a[key] = b[key]
    return a

json_file=open(sys.argv[1])
data = json.load(json_file)

json_file2=open(sys.argv[2])
data2 = json.load(json_file2)

merged = merge_recursively(data, data2)
json.dump(merged, sys.stdout)

json_file.close()
json_file2.close()
