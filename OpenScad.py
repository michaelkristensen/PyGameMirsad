import solid


cube = solid.cube(10)

kugle = solid.sphere(10)

cyl = solid.cylinder(r=10, h=5)

sum = cube + cyl

solid.scad_render_to_file(sum,'min3D.scad')


