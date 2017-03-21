#!/usr/bin/python
# coding: utf-8

from ccad.model import cylinder

outer_diameter = 22.0
inner_diameter = 8.0
thickness = 7.0

part = cylinder(outer_diameter / 2, thickness) - cylinder(inner_diameter / 2, thickness)

if __name__ == '__main__':
    import ccad.display as cd
    v = cd.view()
    v.display(part)
    cd.start()
