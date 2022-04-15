#!/bin/python3

from yaml import load, dump

content = open("./dictionary.yml", "r").read()

output = load(content)

print(output.keys())
