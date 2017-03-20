#!/usr/bin/python
# coding: utf-8

r"""Generation script for F63800ZZ"""

import ccad.model as cm

# General dimensions
outer_diameter = 19.0
inner_diameter = 10.0
thickness = 7.0

# Flange
flange_diameter = 21.0
flange_thickness = 1.5

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