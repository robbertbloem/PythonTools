import re
import numpy
import pathlib
import os


def make_numpy_ndarray(val, verbose = 0):
    """
    Make a numpy.ndarray out of val. 
    
    Types of val that are accepted: 
    
    - int, float, string: make it a list and then numpy.ndarray.
    - list: make it a numpy.ndarray
    - tuple: convert to a list, then numpy.ndarray
    - numpy.ndarray: return directly
    
    Not accepted:
    
    - dict
    
    Notes
    -----
    
    - 2013-03-17/RB: started
    - 2017-03-10/RB: raise a type error for dict, instead of my own error
    - 2019-01-11/RB: copied to SpectraTools
    - 2019-02-15/RB: moved to PythonTools
    
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
    
    Arguments
    ---------
    start : number
    finish : number
    step : number
    match : 'begin', 'middle', 'end'
        See examples. 
    
    
    Examples
    --------


    
        >>> make_range(0, 40, 10, match = "begin")
        [0, 10, 20, 30]
        >>> make_range(0, 40, 10, match = "middle")
        [5, 15, 25, 35]
        >>> make_range(0, 40, 10, match = "end")
        [10, 20, 30, 40]

    Notes
    -----
    
    - 2019-01-xx/RB: started function
    - 2019-02-15/RB: moved to PythonTools
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
    
    Examples 
    --------
    The following input:
    
    >>> "0, 0.1,\\n 1e+3 1e-2"
    [0.0, 0.1, 1000, 0.01]

    Notes
    -----
    
    - 2017-03-09/RB: started
    - 2019-02-15/RB: moved to PythonTools
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



def make_path_and_filename(path, filename = None, extension = None, string_out = False, verbose = 0):
    """
    Concatenate a path and filename (and extension).
    
    Arguments
    ---------
    path : pathlib.Path or str
        Path
    filename : pathlib.Path or str (opt)
        Filename. Optional, can be included in the path.
    extension : str (opt)
        Extension of the file. Optional, can be included in the path or filename. Uses pathlib.with_suffix.
    string_out : bool (False)
        If False (default), the output is a pathlib-object, otherwise the output is a string. 
        
        
    Notes
    -----
    
    - 2019-03-27/RB: started function 
    
    
    """
    
    if verbose > 1:
        print("PythonTools.CommonFunctions.make_path_and_filename()") 


    if os.name == "posix":
        path_type = pathlib.PosixPath
    elif os.name == "nt":
        path_type = pathlib.WindowsPath
      

    if filename is None:
        paf = path
        
    else:
        if type(path) == str:
            path = pathlib.Path(path)
        
        if type(filename) == str:
            filename = pathlib.Path(filename)
            
        paf = path / filename
    
    
    
    if extension is not None:
        
        if extension[0] != ".":
            extension = ".{:s}".format(extension)
            
        paf = paf.with_suffix(extension)
    
    if string_out:
        paf = str(paf)
            
    return paf    
            
    

    



























        