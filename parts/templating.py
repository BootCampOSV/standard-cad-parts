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
