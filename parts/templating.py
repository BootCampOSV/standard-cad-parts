#!/usr/bin/python
# coding: utf-8

r"""Functions for templates handling"""

import os.path
from jinja2 import Environment, FileSystemLoader


def render(template_path, context):
    r"""Render a template using a context

    Parameters
    ----------
    template_path : str
        Full path to a template
    context : dict
        Dict used for template rendering

    Returns
    -------
    The template rendered with the context

    """
    path, filename = os.path.split(template_path)
    return Environment(loader=FileSystemLoader(path or './')).\
        get_template(filename).render(context)


def to_json_string(generators_dict):
    r"""Transform a dictionnary of generators (key = file name no extension;
    value = file content) to a json string

    Parameters
    ----------
    generators_dict : dict
        Dictionnary of generators. The key is the file name without the
        extension; the value is the generator file content

    Returns
    -------
    str : the json string that will replace the {{ generators }} tag in
          library_template.json

    """
    json_ = list()
    length = len(generators_dict.keys())
    for i, (gen_id, content) in enumerate(generators_dict.items()):
        json_.append('"%s"' % gen_id)
        json_.append(' : ')
        json_.append('[')
        for k, line in enumerate(content):
            json_.append('"%s"' % line.replace("\n", ""))

            if k != len(content) - 1:  # no comma separation if last line
                json_.append(",")
        # s += str(content)
        json_.append(']')

        if i != length - 1:  # no comma separation of last generator
            json_.append(",")

        json_.append('\n')
    return "".join(json_)
