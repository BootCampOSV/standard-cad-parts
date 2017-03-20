#!/usr/bin/python
# coding: utf-8

r"""Script that generates the Python scripts (one per possible geometry) from
a JSON file (library.json) that describes each part of the library
"""

import json
import os.path

from parts.templating import render


with open("library.json") as data_file:
    json_file_content = json.load(data_file)

if not os.path.isdir("scripts"):
    os.mkdir("scripts")

for name, context_ in json_file_content["data"].items():
    new_content = render(context_["template"], context_)
    with open("scripts/%s.py" % name, 'w') as f:
        f.write(new_content)
