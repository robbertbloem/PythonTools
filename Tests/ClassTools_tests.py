from __future__ import print_function
from __future__ import division

import argparse
import unittest
import inspect

from imp import reload

import numpy
import matplotlib 
import matplotlib.pyplot as plt

import PythonTools.ClassTools as CT
import PythonTools.Debug as DEBUG

# init argument parser
parser = argparse.ArgumentParser(description='Command line arguments')

# add arguments
parser.add_argument("-v", "--verbose", action="store_true", help="Make PythonTools functions verbose")
parser.add_argument("-r", "--reload", action="store_true", help="Reload modules")
parser.add_argument("-s1", "--skip1", action="store_true", help="Skip testing suite 1")
parser.add_argument("-s2", "--skip2", action="store_true", help="Skip testing suite 2")
parser.add_argument("-s3", "--skip3", action="store_true", help="Skip testing suite 3")

# process
args = parser.parse_args()

# reload
if args.reload:
    reload(CT)
    reload(DEBUG)


class Test_ClassTools_debug(unittest.TestCase):
    """
    Test suite for stuff that prints error messages.
    """
    def setUp(self):
        self.obj = CT.ClassTools()
        
    def test_verbose(self):      
        self.obj.verbose("\ntest verbose", True)

    def test_printError(self):
        self.obj.printError("Error test", inspect.stack())   

    def test_printWarning(self):
        self.obj.printWarning("Warning test", inspect.stack())  



class Test_ClassTools_format_print(unittest.TestCase):
    """
    Test suite for stuff that prints things.
    time stuff is not checked yet
    """
    
    # lists: returned with all elements
    def test_format_print_list_1(self):
        result = CT.format_print([1,2,3])
        self.assertTrue(result == [1,2,3])
        
    def test_format_print_list_2(self):
        result = CT.format_print([[1,1],[1,1]])
        self.assertTrue(result == [[1,1],[1,1]])

    # ndarray: returned as size
    def test_format_print_ndarray_1(self):
        result = CT.format_print(numpy.zeros(1))
        self.assertTrue(result == "1 x 1")

    def test_format_print_ndarray_2(self):
        result = CT.format_print(numpy.zeros(2))
        self.assertTrue(result == "2 x 1")

    def test_format_print_ndarray_3(self):
        result = CT.format_print(numpy.zeros((2,2)))
        self.assertTrue(result == "2 x 2")  
        
    def test_format_print_ndarray_4(self):
        result = CT.format_print(numpy.zeros((2,2,2)))
        self.assertTrue(result == "2 x 2 x 2")         
        
    def test_format_print_ndarray_5(self):
        result = CT.format_print(numpy.zeros((2,2,2,2)))
        self.assertTrue(result == "2 x 2 x 2 x ...")    

    # lists: if an element is something else, it will return that
    def test_format_print_list_3(self):
        result = CT.format_print([numpy.zeros(2), numpy.zeros(3)])
        self.assertTrue(result == ['2 x 1', '3 x 1'])

    # float: will be returned with max 2 decimals
    def test_format_print_float_1(self):
        result = CT.format_print(1.2)
        self.assertTrue(result == 1.2)

    def test_format_print_float_2(self):
        result = CT.format_print(1.23)
        self.assertTrue(result == 1.23)

    def test_format_print_float_3(self):
        result = CT.format_print(1.234)
        self.assertTrue(result == 1.23)

    # numpy.float64: will be returned with max 2 decimals
    def test_format_print_float64_1(self):
        result = CT.format_print(numpy.float64(1.2))
        self.assertTrue(result == 1.2)
    
    def test_format_print_float64_2(self):
        result = CT.format_print(numpy.float64(1.23))
        self.assertTrue(result == 1.23)
    
    def test_format_print_float64_3(self):
        result = CT.format_print(numpy.float64(1.234))
        self.assertTrue(result == 1.23)
    
    # int: returned as itself
    def test_format_print_int_1(self):
        result = CT.format_print(1)
        self.assertTrue(result == 1) 
         
    def test_format_print_int_2(self):
        result = CT.format_print(99999999999999999999999)
        self.assertTrue(result == 99999999999999999999999) 



class Test_ClassTools_format_key(unittest.TestCase):
    """
    Test suite for stuff that prints things.
    """
    def test_format_key_1(self):
        result = CT.format_key("var")
        self.assertTrue(result == "var")

    def test_format_key_2(self):
        result = CT.format_key("_var")
        self.assertTrue(result == "var")

    def test_format_key_3(self):
        result = CT.format_key("__var")
        self.assertTrue(result == "_var")
        
        






if __name__ == '__main__': 
    
    if args.skip1 == False:
        suite = unittest.TestLoader().loadTestsFromTestCase(Test_ClassTools_debug)
        unittest.TextTestRunner(verbosity=1).run(suite)    
    else:
        DEBUG.verbose("Skipping suite 1: debug", True)
        
    if args.skip2 == False:
        suite = unittest.TestLoader().loadTestsFromTestCase(Test_ClassTools_format_print)
        unittest.TextTestRunner(verbosity=1).run(suite)    
    else:
        DEBUG.verbose("Skipping suite 2: format print", True)
        
    if args.skip3 == False:
        suite = unittest.TestLoader().loadTestsFromTestCase(Test_ClassTools_format_key)
        unittest.TextTestRunner(verbosity=1).run(suite)    
    else:
        DEBUG.verbose("Skipping suite 3: format key", True)        
















