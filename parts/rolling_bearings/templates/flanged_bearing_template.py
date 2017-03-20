#!/usr/bin/python
# coding: utf-8

r"""Generation script for {{bearing_name }}"""

import ccad.model as cm

# General dimensions
outer_diameter = {{ outer_diameter }}
inner_diameter = {{ inner_diameter }}
thickness = {{ thickness }}

# Flange
flange_diameter = {{ flange_diameter}}
flange_thickness = {{ flange_thickness }}

part = cm.cylinder(outer_diameter / 2, thickness) - \
       cm.cylinder(inner_diameter / 2, thickness)

flange = cm.cylinder(flange_diameter / 2, flange_thickness) - \
       cm.cylinder(outer_diameter / 2, flange_thickness)
part += flange


if __name__ == "__main__":
    import ccad.display as cd
    v = cd.view()
    v.display(part)
    cd.start()
