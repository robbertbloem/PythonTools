from __future__ import print_function
from __future__ import division
from __future__ import absolute_import

import time

import numpy
import matplotlib 
import matplotlib.pyplot as plt


a = u"fiets"

print(a)
print(type(a))

b = ["auto"]
print(b[0])
print(type(b[0]))



# def format_print(var):
#     """
#     format_print is a helper function for the gatherAttrs function. 
#     There are a few situations:
#         1) var is not a list or an ndarray, it will print the value. This include tuples
#         2) var is an ndarray, the shape will be printed
#         3) var is a time. It will return a readable string with the time.
#         3) the var is a list, it will do recursion to print either 1 or 2
#     Examples:
#         42          => 42
#         "car"       => "car"
#         [1,2]       => [1,2]
#         ndarray     => shape
#         [1,ndarray] => [1, shape]
#     """
#     # list
#     if type(var) == list:
#         typ = list(range(len(var)))
#         for i in range(0, len(var)):
#             typ[i] = format_print(var[i])
#         return typ
#     # ndarray
#     elif type(var) == numpy.ndarray:
#         a = numpy.shape(var)
#         if len(a) == 1: 
#             return str(a[0]) + " x 1"
#         elif len(a) == 2:
#             return str(a[0]) + " x " + str(a[1])
#         elif len(a) == 3:
#             return str(a[0]) + " x " + str(a[1]) + " x " + str(a[2])
# 
#         else: 
#             return str(a[0]) + " x " + str(a[1]) + " x " + str(a[2]) + " x ..."
#     # time
#     elif type(var) == time.struct_time: 
#         var = time.strftime("%a, %d %b %Y %H:%M:%S", var)
#         return var
#     elif type(var) == float:
#         return round(var, 2)
#     elif type(var) == numpy.float64:
#         return round(var, 2)
#     # the rest
#     else:
#         return var
#         
# if __name__ == "__main__":
#     
#     a = [1,2,3]
#     
#     print(a)
#     
#     res = format_print(a)
#     
#     print(res)