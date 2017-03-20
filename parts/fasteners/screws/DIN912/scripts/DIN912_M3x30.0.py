#!/usr/bin/python
# coding: utf-8

r"""Generation script for DIN912_M3x30.0"""

from __future__ import division

import ccad.model as cm

length = 30.0
threaded_length = 18.0
unthreaded_diameter = 3.0
threaded_diameter = 2.675
head_diameter = 5.5
head_height = 3.0
key_size = 2.5
socket_depth = 1.3

if length - threaded_length > 0.:
    body = cm.cylinder(threaded_diameter / 2, length) + \
           cm.cylinder(unthreaded_diameter / 2, length - threaded_length)
else:
    body = cm.cylinder(threaded_diameter / 2, length)

socket = cm.translated(cm.prism(cm.filling
                                # ngon is written in a circle of a given radius,
                                # the socket definition is the diameter of the
                                # circle written in the hexagon
                                # -> multiply by 2 / sqrt(3)
                                (cm.ngon(2 / 3**.5 * key_size / 2., 6)),
                                (0, 0, socket_depth)),
                       (0, 0, -head_height))

head = cm.translated(cm.cylinder(head_diameter / 2., head_height),
                     (0, 0, -head_height)) - socket
part = head + body


if __name__ == "__main__":
    import ccad.display as cd
    v = cd.view()
    v.display(part)
    cd.start()
