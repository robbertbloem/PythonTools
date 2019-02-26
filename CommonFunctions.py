import re
import numpy


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



def make_range(start, finish, step, match = "middle", verbose = 0):
    """
    In most cases, start, stop and step do not match. For example: numpy.arange(0, 40, 10) >>> [0, 10, 20, 30]
    
    
    
    INPUT:
    - match: 
        - 'begin', the behavior is as numpy.arange() >>> [0, 10, 20, 30]
        - 'middle': >>> [5, 15, 25, 35]
        - 'end': >>>[10, 20, 30, 40]

    2019-01-xx/RB: started function
    2019-02-15/RB: moved to PythonTools
    """
    if verbose > 1:
        print("SpectraTools.Resources.CommonFunctions:make_range()")
        
    if match == "begin":
        return numpy.arange(start, finish, step)
    
    elif match == "middle":        
        n_steps = (finish - start) // step        
        r = (finish - start - (n_steps - 1) * step) / 2        
        return numpy.arange(start + r, finish, step)
        
    elif match == "end":
        x = numpy.arange(start, finish, step)
        return x + (finish - x[-1])
  

        

def string_with_numbers_to_list(string):
    """
    Receive a string with numbers, for example from a file, and make a ndarray out of it. The output type is always float. Commas and spaces indicate the separation between numbers and can be mixed. Newlines are removed.
    
    string = "0, 0.1,\n 1e+3 1e-2"
    output: [0.0, 0.1, 1000, 0.01]

    CHANGELOG:
    20170309/RB: started
    2019-02-15/RB: moved to PythonTools
    """
    
    string = string.replace("\n", " ")
    # remove everything, except \d (numbers), \s (spaces), . (decimal), e (exponent), +, - (signs)
    non_decimal = re.compile(r'[^\d\s.eE+-]+')
    res = non_decimal.sub('', string)
    data = res.split(" ")
    # remove excess spaces
    data = list(filter(None, data))

    data = numpy.array(data)
    data = data.astype(float)

    return data   


        