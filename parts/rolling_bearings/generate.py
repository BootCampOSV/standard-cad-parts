#!/usr/bin/python
# coding: utf-8

r"""Script that generates the Python scripts (one per possible geometry) from
a JSON file (library.json) that describes each part of the library
"""

import json
import os

from parts.templating import render, to_json_string


def create_library_json():
    r"""Use library_template.json to create library.json using the Python
    generator files in the generators subdirectory"""

    generators = dict()

    # iterate over the files in the templates folder
    for generator_file in os.listdir("generators"):
        # use the file name without extension as the generator id
        generator_id = os.path.splitext(generator_file)[0]

        with open("generators/%s" % generator_file) as gf:
            generators[generator_id] = gf.readlines()

    context = dict()
    context["generators"] = to_json_string(generators)

    with open("library.json", 'w') as library_json:
        library_json.write(render("library_template.json", context))


def create_scripts():
    r"""Create a geometry generation script for each part defined
    in library.json"""
    if not os.path.isdir("scripts"):
        os.mkdir("scripts")

    with open("library.json") as data_file:
        json_file_content = json.load(data_file)

    json_generators = json_file_content["generators"]

    for name, context_ in json_file_content["data"].items():
        with open("tmp.py", "w") as tmp_file:
            tmp_file.write("#!/usr/bin/python\n")
            tmp_file.write("# coding: utf-8\n\n")
            tmp_file.write("from ccad.model import cylinder\n\n")
            tmp_file.write("\n".join(json_generators[context_["generator"]]))
            tmp_file.write("\n\nif __name__ == '__main__':\n")
            tmp_file.write("    import ccad.display as cd\n")
            tmp_file.write("    v = cd.view()\n")
            tmp_file.write("    v.display(part)\n")
            tmp_file.write("    cd.start()\n\n")

        # Use tmp.py as a template for context_ and write the results to the
        # part script
        with open("scripts/%s.py" % name, 'w') as f:
            f.write(render("tmp.py", context_))
    os.remove("tmp.py")


create_library_json()
create_scripts()
