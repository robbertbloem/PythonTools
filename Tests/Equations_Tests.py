from importlib import reload
import inspect
import os
import warnings
import unittest

import numpy


import PythonTools.Equations as EQ

reload(EQ)

# {"label": "", "A": [], "x": numpy.array([]), "test": numpy.array([])},     
# {"label": "", "A": [], "x": numpy.array([]), "test": numpy.array([])},     
# {"label": "", "A": [], "x": numpy.array([]), "test": numpy.array([])},     

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
            {"label": "", "A": [1], "x": numpy.array([]), "test": numpy.array([])},
            # {"label": "", "A": [], "x": numpy.array([]), "test": numpy.array([])},
        ]
        
        for t in tests:
            y = EQ.polynomial(t["A"], t["x"])
            with self.subTest(t["label"]):
                self.assertTrue(numpy.allclose(y, t["test"]))

    def test_errors(self):
        tests = [
            # {"label": "Test 1", "A": [1], "x": numpy.array([]), "test": numpy.array([1])},
            # {"label": "Test 2", "A": [0,2,1,0], "x": numpy.array([0, 1]), "test": numpy.array([2,2])},
            # {"label": "", "A": [], "x": numpy.array([]), "test": numpy.array([])},            
        ]
        
        for t in tests:
            with self.subTest(t["label"]):
                with self.assertRaises(Exception):
                    y = EQ.polynomial(t["A"], t["x"])

                
class Test_cos(unittest.TestCase):

    def setUp(self):
        self.verbose = 0



    def test_basic(self):
        """
        Basic test
        """
        tests = [
            {"label": "Test 1", "A": [0,1,1,0], "x": numpy.array([0, 1]), "test": numpy.array([1,1])},
            {"label": "Test 2", "A": [0,2,1,0], "x": numpy.array([0, 1]), "test": numpy.array([2,2])},
            # {"label": "", "A": [], "x": numpy.array([]), "test": numpy.array([])},            
        ]
        
        for t in tests:
            with self.subTest(t["label"]):
                y = EQ.cos(t["A"], t["x"])
                # print(t["label"], y)
                self.assertTrue(numpy.allclose(y, t["test"]))        

                
    def test_errors(self):
        tests = [
            {"label": "Test 1", "A": [0,1,1], "x": numpy.array([0, 1]), "test": numpy.array([1,1])},
            # {"label": "Test 2", "A": [0,2,1,0], "x": numpy.array([0, 1]), "test": numpy.array([2,2])},
            # {"label": "", "A": [], "x": numpy.array([]), "test": numpy.array([])},            
        ]
        
        for t in tests:
            with self.subTest(t["label"]):
                with self.assertRaises(Exception):
                    y = EQ.cos(t["A"], t["x"])

class Test_single_exp(unittest.TestCase):

    def setUp(self):
        self.verbose = 0

    def test_basic(self):
        """
        Basic test
        """
        tests = [
            {"label": "Test 1", "A": [1,1], "x": numpy.array([1,2]), "test": numpy.array([numpy.exp(-1), numpy.exp(-2)])},
            {"label": "Test 2 empty x", "A": [1,1], "x": numpy.array([]), "test": numpy.array([])},
        ]
        
        for t in tests:
            y = EQ.single_exp(t["A"], t["x"])
            # print(t["label"], y)
            with self.subTest(t["label"]):
                self.assertTrue(numpy.allclose(y, t["test"]))

    def test_errors(self):
        tests = [
            {"label": "Test 1 A short", "A": [1], "x": numpy.array([1,2]), "test": numpy.array([numpy.exp(-1), numpy.exp(-2)])},  
            {"label": "Test 2 A long", "A": [1,1,1], "x": numpy.array([1,2]), "test": numpy.array([numpy.exp(-1), numpy.exp(-2)])},              
        ]
        
        for t in tests:
            with self.subTest(t["label"]):
                with self.assertRaises(Exception):
                    y = EQ.single_exp(t["A"], t["x"])

class Test_gaussian(unittest.TestCase):

    def setUp(self):
        self.verbose = 0

    def test_basic(self):
        """
        Basic test
        """
        tests = [
            {"label": "Test 1", "A": [1,1,1,1], "x": numpy.array([1,2]), "test": numpy.array([1.39894228, 1.24197072])},
            {"label": "Test 2", "A": [numpy.sqrt(0.5),0,0,1.77245385], "x": numpy.array([0]), "test": numpy.array([1])},
            {"label": "Test 3 empty x", "A": [1,1,1,1], "x": numpy.array([]), "test": numpy.array([])},
        ]
        
        for t in tests:
            y = EQ.gaussian(t["A"], t["x"])
            # print(t["label"], y)
            with self.subTest(t["label"]):
                self.assertTrue(numpy.allclose(y, t["test"]))

    def test_errors(self):
        tests = [
            {"label": "Test 1 A short", "A": [1,1,1], "x": numpy.array([1,2]), "test": numpy.array([1, 1])},
            {"label": "Test 1 A Long", "A": [1,1,1,1,1], "x": numpy.array([1,2]), "test": numpy.array([1, 1])},
        ]
        
        for t in tests:
            with self.subTest(t["label"]):
                with self.assertRaises(Exception):
                    y = EQ.gaussian(t["A"], t["x"])





# class Test_XXX(unittest.TestCase):

    # def setUp(self):
        # self.verbose = 0

    # def test_basic(self):
        # """
        # Basic test
        # """
        # tests = [
            # {"label": "Test ", "A": [], "x": numpy.array([]), "test": numpy.array([])},
        # ]
        
        # for t in tests:
            # y = EQ.XXX(t["A"], t["x"])
            # print(t["label"], y)
            # with self.subTest(t["label"]):
                # self.assertTrue(numpy.allclose(y, t["test"]))

    # def test_errors(self):
        # tests = [
            # {"label": "Test ", "A": [], "x": numpy.array([]), "test": numpy.array([])},
        # ]
        
        # for t in tests:
            # with self.subTest(t["label"]):
                # with self.assertRaises(Exception):
                    # y = EQ.XXX(t["A"], t["x"])                    
                
                
if __name__ == '__main__': 
    verbosity = 1

    unittest.main()
    