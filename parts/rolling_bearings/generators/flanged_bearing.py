outer_diameter = {{ outer_diameter }}
inner_diameter = {{ inner_diameter }}
thickness = {{ thickness }}

flange_diameter = {{ flange_diameter}}
flange_thickness = {{ flange_thickness }}

part = cylinder(outer_diameter / 2, thickness) - cylinder(inner_diameter / 2, thickness)

flange = cylinder(flange_diameter / 2, flange_thickness) - cylinder(outer_diameter / 2, flange_thickness)
part += flange
