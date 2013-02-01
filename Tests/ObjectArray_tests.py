from __future__ import print_function
from __future__ import division

import argparse
import unittest

import numpy
import matplotlib 
import matplotlib.pyplot as plt

import PythonTools.ObjectArray as OA
import PythonTools.Debug as DEBUG
import PythonTools.ClassTools as CT # only imported to allow for reload

# init argument parser
parser = argparse.ArgumentParser(description='Command line arguments')

# add arguments
parser.add_argument("-v", "--verbose", action="store_true", help="Increase output verbosity")
parser.add_argument("-r", "--reload", action="store_true", help="Reload modules")
parser.add_argument("-s1", "--skip1", action="store_true", help="Skip testing suite 1")
parser.add_argument("-s2", "--skip2", action="store_true", help="Skip testing suite 2")

# process
args = parser.parse_args()

# reload
if args.reload:
    reload(OA)
    reload(DEBUG)
    reload(CT)



# @unittest.skipIf(args.skip1 == True, "Skipping suite 1")
class Test_ObjectArray(unittest.TestCase):

    #############
    ### SETUP ###
    #############
    def setUp(self):
        
        self.flag_verbose = args.verbose
        
        self.oa = OA.objectarray("test")
        
        a = OA.testobject("Auto", "a", "power", flag_verbose = self.flag_verbose)
        b = OA.testobject("Boot", "b", "power", flag_verbose = self.flag_verbose)
        c = OA.testobject("Fiets", "c", "human", flag_verbose = self.flag_verbose)
        
        self.oa.add_object(a, flag_verbose = self.flag_verbose)
        self.oa.add_object(b, flag_verbose = self.flag_verbose)
        self.oa.add_object(c, flag_verbose = self.flag_verbose)
        

    ###########################
    ### TEST ADDING OBJECTS ###
    ###########################
    def test_add_object_1(self):
        """
        Add object with new obj_id
        """
        a = OA.testobject("Brommer", "d", "power", flag_verbose = self.flag_verbose)
        result = self.oa.add_object(a, flag_verbose = self.flag_verbose)
        self.assertTrue(["a", "b", "c", "d"] ==  self.oa.obj_id_array and result == True) 
         
    
    def test_add_object_2(self):
        """
        Add object with same obj_id
        """
        a = OA.testobject("Boot", "a", "power", flag_verbose = self.flag_verbose)
        DEBUG.verbose("\nError is intentional", True)
        result = self.oa.add_object(a, flag_verbose = self.flag_verbose)
        self.assertTrue(["a", "b", "c"] ==  self.oa.obj_id_array and result == False) 
        
    
    def test_add_object_3(self):
        """
        Add object without obj_id
        """
        oa = OA.objectarray("test_new")
        DEBUG.verbose("\nError is intentional", True)
        result = oa.add_object(1, flag_verbose = self.flag_verbose)
        self.assertFalse(result) 


    #############################
    # TEST SORTING BY SUBTYPE ###
    #############################
    def test_object_with_sub_type_1(self):
        """
        Test if objects with sub_type 'power' are found. 
        """
        sub_type = "power"
        array = self.oa.object_with_sub_type(sub_type = sub_type, flag_verbose = self.flag_verbose)        
        self.assertTrue(self.oa.obj_array[array[0]].sub_type == sub_type and self.oa.obj_array[array[1]].sub_type == sub_type)
        
        
    def test_object_with_sub_type_2(self):
        """
        Test if objects with sub_type 'x' are found - there should be none. This raises a warning. The resulting array has length zero.
        """
        sub_type = "x"
        DEBUG.verbose("\nWarning is intentional", True) 
        array = self.oa.object_with_sub_type(sub_type = sub_type, flag_verbose = self.flag_verbose)       
        self.assertTrue(len(array) == 0)        




# @unittest.skipIf(args.skip2 == True, "Skipping suite 2")
class Test_ObjectArray_pickle(unittest.TestCase):

    #############
    ### SETUP ###
    #############
    def setUp(self):
        
        self.path_and_filename = "/Users/robbert/Developer/PythonTools/temp/test.pickle"
        self.flag_verbose = args.verbose

        oa = OA.objectarray("test")
        
        a = OA.testobject("Auto", "a", "power", flag_verbose = self.flag_verbose)
        b = OA.testobject("Boot", "b", "power", flag_verbose = self.flag_verbose)
        c = OA.testobject("Fiets", "c", "human", flag_verbose = self.flag_verbose)
        
        oa.add_object(a, flag_verbose = self.flag_verbose)
        oa.add_object(b, flag_verbose = self.flag_verbose)
        oa.add_object(c, flag_verbose = self.flag_verbose)
        
        oa.save_objectarray(self.path_and_filename, flag_verbose = self.flag_verbose)
        
        self.obj_id_array = oa.obj_id_array


    #################################
    ### TEST LOADING OBJECT ARRAY ###
    #################################
    def test_load_objectarray_1(self):
        """
        Test if object are correctly ordered.
        obj_id_array_in is same as pickle
        """
        oa = OA.objectarray("test_new")
        oa.load_objectarray(self.path_and_filename, obj_id_array_in = self.obj_id_array, flag_verbose = self.flag_verbose) 
        self.assertTrue(["a", "b", "c"] ==  oa.obj_id_array)      

    def test_load_objectarray_2(self):  
        """
        Test if object are correctly ordered.
        obj_id_array_in misses one obj_id compared to pickle. The object array should miss that object.
        """
        obj_id_array = ["a", "b"]
        oa = OA.objectarray("test_new")
        oa.load_objectarray(self.path_and_filename, obj_id_array_in = obj_id_array, flag_verbose = self.flag_verbose) 
        self.assertTrue(["a", "b"] ==  oa.obj_id_array)      

    def test_load_objectarray_3(self):  
        """
        Test if object are correctly ordered.
        obj_id_array_in has one element too much compared to pickle. The object array will only contain the elements of the pickle
        """
        obj_id_array = ["a", "b", "c", "d"]
        oa = OA.objectarray("test_new")
        oa.load_objectarray(self.path_and_filename, obj_id_array_in = obj_id_array, flag_verbose = self.flag_verbose) 
        self.assertTrue(["a", "b", "c"] ==  oa.obj_id_array)   

    def test_load_objectarray_4(self):  
        """
        Test if object are correctly ordered.
        obj_id_array_in has one element too much compared to pickle. The object array will only contain the elements of the pickle
        """
        obj_id_array = ["a", "b", "d"]
        oa = OA.objectarray("test_new")
        oa.load_objectarray(self.path_and_filename, obj_id_array_in = obj_id_array, flag_verbose = self.flag_verbose) 
        self.assertTrue(["a", "b"] ==  oa.obj_id_array)


        

    



if __name__ == '__main__':

    if args.skip1 == False:
        suite = unittest.TestLoader().loadTestsFromTestCase(Test_ObjectArray)
        unittest.TextTestRunner(verbosity=2).run(suite)    
    else:
        DEBUG.verbose("Skipping suite 1", True)
    
    
    if args.skip2 == False:
        suite = unittest.TestLoader().loadTestsFromTestCase(Test_ObjectArray_pickle)
        unittest.TextTestRunner(verbosity=2).run(suite)    
    else:
        DEBUG.verbose("Skipping suite 2", True)    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    