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

metric_thread_specs = json_file_content["metric_threads"]["coarse"]

for metric_thread, dimensions in json_file_content["data"]["DIN912"].items():
    for length in dimensions['lengths']:
        new_content = render("templates/DIN912_template.py",
                             {'screw_description': "DIN912_%sx%s" % (metric_thread, str(length)),
                              'length': length,
                              'thread_length_minimal': dimensions['thread-length-minimal'],
                              'diameter_major': metric_thread_specs[metric_thread]['diameter-major'],
                              'diameter_pitch': metric_thread_specs[metric_thread]['diameter-pitch'],
                              'head_diameter': dimensions['head-diameter'],
                              'head_height': dimensions['head-height'],
                              'key_size': dimensions['key-size'],
                              'socket_depth': dimensions['socket-depth']})
        with open("scripts/DIN912_%sx%s.py" % (metric_thread, str(length)), 'w') as f:
            f.write(new_content)


