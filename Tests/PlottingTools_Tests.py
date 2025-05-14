import importlib

import argparse
import unittest

import numpy
import matplotlib 
import matplotlib.pyplot as plt

import PythonTools.PlottingTools as PT

importlib.reload(PT)

class Test_make_coordinates(unittest.TestCase):
    """
    See if making coordinates works

    CHANGELOG:
    20130317/RB: started the suite

    """

    def setUp(self):
        """
        Toggle verbose using the command line. 
        """

        self.flag_verbose = 1

    def test_single_plot_10(self):
        """
        Simple test
        Single plot in middle
        inch_per_unit = 1
        """
        
        inch_per_unit = 1
        x_units = 4
        y_units = 4
        left = 1
        bottom = 1
        width = 2
        height = 2
        
        figsize, coords = PT.make_coordinates(inch_per_unit, x_units, y_units, left, bottom, width, height)
        
        self.assertEqual(figsize, (4,4))
        self.assertEqual(coords, [(0.25, 0.25, 0.5, 0.5)])
        

    def test_single_plot_05(self):
        """
        See if changing inch_per_init works
        Single plot in middle
        inch_per_unit = 0.5
        """
        inch_per_unit = 0.5
        x_units = 4
        y_units = 4
        left = 1
        bottom = 1
        width = 2
        height = 2
        
        figsize, coords = PT.make_coordinates(inch_per_unit, x_units, y_units, left, bottom, width, height)
        
        self.assertEqual(figsize, (2,2))
        self.assertEqual(coords, [(0.25, 0.25, 0.5, 0.5)])
    

    def test_double_h_plot_1(self):
        """
        Two plots, equal sizes
        |1<2>2<2>1| is |1/8<1/4>1/4<1/4>1/8|
        """
        inch_per_unit = 1.0
        x_units = 8
        y_units = 4
        left = [1,5]
        bottom = 1
        width = 2
        height = 2
        
        figsize, coords = PT.make_coordinates(inch_per_unit, x_units, y_units, left, bottom, width, height)
                
        self.assertEqual(figsize, (8,4))
        self.assertEqual(coords, [(0.125, 0.25, 0.25, 0.5), (0.625, 0.25, 0.25, 0.5)])




    def test_double_h_plot_2(self):
        """
        Two plots
        |1<3>1<4>1| is |0.1<0.3>0.1<0.4>0.1|

        """
        inch_per_unit = 1.0
        x_units = 10
        y_units = 4
        left = [1,5]
        bottom = 1
        width = [3,4]
        height = 2
        
        figsize, coords = PT.make_coordinates(inch_per_unit, x_units, y_units, left, bottom, width, height)
                
        self.assertEqual(figsize, (10,4))
        self.assertEqual(coords, [(0.1, 0.25, 0.3, 0.5), (0.5, 0.25, 0.4, 0.5)])


    def test_four_plots_simple(self):
        """
        Four plots - simple
        01234
        3 x x
        2xxxx
        1 x x 
        0xxxx
    
        """
        inch_per_unit = 1.0
        x_units = 5
        y_units = 5
        left = [1,3]
        bottom = [3,3,1,1]
        width = 1
        height = 1
        
        figsize, coords = PT.make_coordinates(inch_per_unit, x_units, y_units, left, bottom, width, height)
    
        c = [(0.2, 0.6, 0.2, 0.2), (0.6, 0.6, 0.2, 0.2), (0.2, 0.2, 0.2, 0.2), (0.6, 0.2, 0.2, 0.2)]
        
        self.assertEqual(figsize, (5,5))
        self.assertTrue(numpy.allclose(numpy.array(coords), numpy.array(c)))


    def test_four_plots_complex(self):
        """
        Four plots - quite complex
        01234567
        6   x  x
        5   x  x
        4xxxx  x
        3  xxxxx
        2  x   x
        1  x   x
        0xxxxxxx
    
        """
        inch_per_unit = 1.0
        x_units = 8
        y_units = 8
        left = [1,5,1,4]
        bottom = [5,4,1,1]
        width = [3,2,2,3]
        height = [2,3,3,2]
        
        figsize, coords = PT.make_coordinates(inch_per_unit, x_units, y_units, left, bottom, width, height)

        r = 0.125
        c = [(r, 5*r, 3*r, 2*r), (5*r, 4*r, 2*r, 3*r), (r, r, 2*r, 3*r), (4*r, r, 3*r, 2*r)]
                
        self.assertEqual(figsize, (8,8))
        self.assertEqual(coords, c)


    def test_three_plots(self):
        """
        Three plots, but width has only two elements. 
        
        01234567
        x x  x x

        """
        inch_per_unit = 1.0
        x_units = 8
        y_units = 1
        left = [1,3,6]
        bottom = 0
        width = [1,2]
        height = 1
        
        figsize, coords = PT.make_coordinates(inch_per_unit, x_units, y_units, left, bottom, width, height)
    
        r = 0.125
        c = [(r, 0, r, 1), (3*r, 0, 2*r, 1), (6*r, 0, r, 1)]
                
        self.assertEqual(figsize, (8,1))
        self.assertEqual(coords, c)













    
class Test_make_numpy_ndarray(unittest.TestCase):
    """
    

    CHANGELOG:
    20130317/RB: started the suite

    """

    def setUp(self):
        """
        Toggle verbose using the command line. 
        
        int, float, string: make it a list and then numpy.ndarray.
        list: make it a numpy.ndarray
        tuple: convert to a list, then numpy.ndarray
        numpy.ndarray: return directly
        dict: give error
        
        self.values = [[val, type of return]], if type of return is numpy.ndarray, leave it away.
        
        """

        self.flag_verbose = 1
        
        self.values = [
            [1],                        # int
            [0.2],                      # float
            ["fiets"],                  # string
            [(1,2)],                    # tuple
            [[1]],                      # short list
            [[1,2]],                    # longer list
            [numpy.array([1,2])],       # numpy.ndarray
            [{"a": 1, "b": 2}, bool]    # dict
        ]


    def test_values(self):
        
        for i in self.values:
            
            if len(i) == 1:
                check_type = numpy.ndarray 
            else:
                check_type = i[1]  
                print("Error is intentional")           
            
            result = PT.make_numpy_ndarray(i[0])
            
            self.assertEqual(type(result), check_type)  
            
 
class Test_find_longest_list(unittest.TestCase):
    """
    Find the longest list for a series of lists
    
    CHANGELOG:
    20130317/RB: started the suite

    """

    def setUp(self):
        """
        Toggle verbose using the command line. 

        """
        self.flag_verbose = 1

        self.a = [1]
        self.b = [1,2]
        self.c = [1,2,3]
        
        self.d = numpy.array([1,2])
        self.e = numpy.array([1,2,3,4])

    def test_1(self):
        result = PT.find_longest_list(self.a, self.b, self.c)
        self.assertEqual(result, 3) 

    def test_2(self):
        result = PT.find_longest_list(self.a, self.c, self.d)
        self.assertEqual(result, 3)           

    def test_3(self):
        result = PT.find_longest_list(self.a, self.b, self.e)
        self.assertEqual(result, 4)     

    def test_4(self):
        result = PT.find_longest_list(self.a)
        self.assertEqual(result, 1)   

        
        

class Test_make_figures(unittest.TestCase):

    def setUp(self):
        pass
        
        
    def test(self):
        
        figures = [
            {"label": "Two axes", "u": 1/2.54, "fig_w": 20, "fig_h": 15, "l": 1.8, "b": [8, 1.2], "ax_w": 17.5, "ax_h": [5.5]}, 
            {"label": "Two axes and twinx", "u": 1/2.54, "fig_w": 20, "fig_h": 15, "l": 1.8, "b": [8, 1.2], "ax_w": 16, "ax_h": [5.5], "twinx": [0]},
            {"label": "Two axes, twinx, twiny", "u": 1/2.54, "fig_w": 20, "fig_h": 15, "l": 1.8, "b": [8, 1.2], "ax_w": 16, "ax_h": [5.5], "twinx": [0], "twiny": [0]},
            {"label": "Documentation", "u": 1/2.54, "fig_w": 20, "fig_h": 15, "l": 1.8, "b": [5, 1.2], "ax_w": 16, "ax_h": [6,3], "twinx": [0]},  
            {"label": "No u", "fig_w": 20, "fig_h": 15, "l": 1.8, "b": [5, 1.2], "ax_w": 16, "ax_h": [6,3], "twinx": [0]},              
        ]
        fig, ax = PT.make_figures(figures, label = True)
        
        for fig_i, f in enumerate(figures):
            fig[fig_i].suptitle(f["label"])

        
    def test_no_list(self):

        figures = {"label": "Two axes", "u": 1/2.54, "fig_w": 20, "fig_h": 15, "l": 1.8, "b": [8, 1.2], "ax_w": 17.5, "ax_h": [5.5]}     
        fig, ax = PT.make_figures(figures, label = True)
        
        fig_i = 0
        fig[fig_i].suptitle(figures["label"])        
    
    
    def test_named_sizes(self):
        figures = [
            "wide",
            "A4_landscape",
            "A4_portrait",
            "standard",
        ]
        fig, ax = PT.make_figures(figures, label = True)
        
        for fig_i, f in enumerate(figures):
            fig[fig_i].suptitle(f)        
        
    def test_unknown_named_size(self):
        
        figures = [
            "fiets"
        ]
        
        with self.assertWarns(UserWarning) as cm:        
            fig, ax = PT.make_figures(figures, label = True)
            for fig_i, f in enumerate(figures):
                fig[fig_i].suptitle(f)   
        
    def test_missing_params(self):
        
        figures = [
            {"label": "Missing fig_w", "u": 1/2.54, "fig_h": 15, "l": 1.8, "b": 1.2, "ax_w": 17.5, "ax_h": 12.5},
        ]
        
        with self.assertRaises(KeyError) as cm:        
            fig, ax = PT.make_figures(figures, label = True)

        
        
if __name__ == '__main__': 

    verbosity = 1

    plt.close("all")
    
    if 1:
        suite = unittest.TestLoader().loadTestsFromTestCase(Test_make_coordinates)
        unittest.TextTestRunner(verbosity = verbosity).run(suite)  


    if 1:
        suite = unittest.TestLoader().loadTestsFromTestCase(Test_make_numpy_ndarray)
        unittest.TextTestRunner(verbosity = verbosity).run(suite)  


    if 1:
        suite = unittest.TestLoader().loadTestsFromTestCase(Test_find_longest_list)
        unittest.TextTestRunner(verbosity = verbosity).run(suite)  

    if 1:
        suite = unittest.TestLoader().loadTestsFromTestCase(Test_make_figures)
        unittest.TextTestRunner(verbosity = verbosity).run(suite)  


    plt.show()





















