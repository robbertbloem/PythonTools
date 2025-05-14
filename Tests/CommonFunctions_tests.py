import importlib 
import pathlib
import inspect
import os
import warnings
import unittest

import numpy
import matplotlib 
import matplotlib.pyplot as plt

import PythonTools as PT

importlib.reload(PT)


class Test_save_data(unittest.TestCase):

    def setUp(self):
        self.verbose = 1
        self.path = pathlib.Path("Testdata\save_data")
        


        
        
if __name__ == '__main__': 
    verbosity = 2
    
    
    if 1:
        """
        + __init__
        """
        suite = unittest.TestLoader().loadTestsFromTestCase(Test_init)
        unittest.TextTestRunner(verbosity=verbosity).run(suite)