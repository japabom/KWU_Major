# -*- coding: utf-8 -*-
"""
Created on Mon Oct 28 14:46:39 2019

@author: kang
"""

from vec import Vec
from geometry_lab import *
from image_mat_util import *

points, colors = file2mat('python_small.png')
mat2display(points, colors)

# translation
mat_trans = translation(10, 20)
print(mat_trans)

points_trans = mat_trans * points
mat2display(points_trans, colors)

# scaling
mat_scale = scale(2.5, 0.8)
print(mat_scale)

points_scale = mat_scale * points
mat2display(points_scale, colors)

# rotation
mat_rot = rotation(math.pi / 4)
print(mat_rot)

points_rot = mat_rot * points
mat2display(points_rot, colors)

# reflection
mat_refX = reflect_x()
mat_refY = reflect_y()

print(mat_refX)
print(mat_refY)

# grayscale
mat_gray = grayscale()
print(mat_gray)

colors_gray = mat_gray * colors
mat2display(points, colors_gray)

# reflection about axis
p1 = Vec({'x','y','u'}, {'x':0, 'y':50, 'u':1})
p2 = Vec({'x','y','u'}, {'x':100, 'y':50, 'u':1})

mat_ref = reflect_about(p1, p2)
print(mat_ref)

points_ref = mat_ref * points
mat2display(points_ref, colors_gray)

