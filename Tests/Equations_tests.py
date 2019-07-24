from importlib import reload
import inspect
import os
import warnings
import unittest

import numpy


import PythonTools.Equations as EQ

reload(EQ)



class Test_polynomial(unittest.TestCase):

    def setUp(self):
        self.verbose = 0



    def test_basic(self):
        """
        Basic test
        """
        tests = [
            {"label": "Test 1", "A": [1], "x": numpy.array([1]), "test": numpy.array([1])},
            {"label": "Test 2", "A": [1,1], "x": numpy.array([1]), "test": numpy.array([2])},
            {"label": "Test 3", "A": [1,1], "x": numpy.array([1,2]), "test": numpy.array([2,3])},
            {"label": "Test 4", "A": [1,2], "x": numpy.array([1,2]), "test": numpy.array([3,5])},
            {"label": "Test 5", "A": [1,1,1], "x": numpy.array([1,2]), "test": numpy.array([3, 7])},
            {"label": "Test 6", "A": [0], "x": numpy.array([1]), "test": numpy.array([0])},
            {"label": "Test 7 A is ndarray", "A": numpy.array([1,1]), "x": numpy.array([1,2]), "test": numpy.array([2,3])},
            {"label": "Test 8 x is list", "A": [1,1], "x": [1,2], "test": numpy.array([2,3])},
            {"label": "Test 9 x is tuple", "A": [1,1], "x": (1,2), "test": numpy.array([2,3])},
            # {"label": "", "A": [], "x": numpy.array([]), "test": numpy.array([])},
            # {"label": "", "A": [], "x": numpy.array([]), "test": numpy.array([])},
            # {"label": "", "A": [], "x": numpy.array([]), "test": numpy.array([])},
        ]
        
        for t in tests:
            y = EQ.polynomial(t["A"], t["x"])
            with self.subTest(t["label"]):
                self.assertTrue(numpy.allclose(y, t["test"]))
        
        
        
if __name__ == '__main__': 
    verbosity = 1

    
    if 1:
        suite = unittest.TestLoader().loadTestsFromTestCase(Test_polynomial)
        unittest.TextTestRunner(verbosity=verbosity).run(suite)            