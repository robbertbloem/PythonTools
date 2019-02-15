
# from importlib import reload
# import inspect
# import os
# import warnings

# import re
import numpy
# import matplotlib 



def make_numpy_ndarray(val, verbose = 0):
    """
    Make a numpy.ndarray out of val. 
    
    Types of val that are accepted:        
    int, float, string: make it a list and then numpy.ndarray.
    list: make it a numpy.ndarray
    tuple: convert to a list, then numpy.ndarray
    numpy.ndarray: return directly
    
    Not accepted:
    dict
    
    CHANGELOG:
    2013-03-17/RB: started
    2017-03-10/RB: raise a type error for dict, instead of my own error
    2019-01-11/RB: copied to SpectraTools
    2019-02-15/RB: moved to PythonTools
    """
    if verbose > 1:
        print("PythonTools.CommonFunctions:make_numpy_ndarray()")
            
    if type(val) == numpy.ndarray:
        return val
    elif type(val) == list:
        return numpy.array(val)
    elif type(val) == dict:
        raise TypeError("Value can't be a dict")
    elif type(val) == tuple:
        return numpy.array(list(val))
    else:
        return numpy.array([val]) 