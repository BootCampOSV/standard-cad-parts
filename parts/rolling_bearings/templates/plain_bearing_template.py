#!/usr/bin/python
# coding: utf-8

r"""Generation script for {{bearing_name }}"""

import ccad.model as cm

# General dimensions
outer_diameter = {{ outer_diameter }}
inner_diameter = {{ inner_diameter }}
thickness = {{ thickness }}

part = cm.cylinder(outer_diameter / 2, thickness) - \
       cm.cylinder(inner_diameter / 2, thickness)


if __name__ == "__main__":
    import ccad.display as cd
    v = cd.view()
    v.display(part)
    cd.start()

