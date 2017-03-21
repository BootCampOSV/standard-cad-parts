#!/usr/bin/python
# coding: utf-8

from ccad.model import cylinder

outer_diameter = 19.0
inner_diameter = 10.0
thickness = 7.0

flange_diameter = 21.0
flange_thickness = 1.5

part = cylinder(outer_diameter / 2, thickness) - cylinder(inner_diameter / 2, thickness)

flange = cylinder(flange_diameter / 2, flange_thickness) - cylinder(outer_diameter / 2, flange_thickness)
part += flange

if __name__ == '__main__':
    import ccad.display as cd
    v = cd.view()
    v.display(part)
    cd.start()
