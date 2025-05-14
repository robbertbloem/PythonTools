import importlib 
import pathlib
import inspect
import os
import warnings
import unittest

import numpy
import matplotlib 
import matplotlib.pyplot as plt

import PythonTools.CommonFunctions as CF

importlib.reload(CF)


class Test_make_path_and_filename(unittest.TestCase):

    def setUp(self):
        self.verbose = 1
        

        
#         print(type(self.path_str))
        
        
                
        
    def test_simple(self):
    
        path = pathlib.Path(__file__).parent
         
        p_pl = path.joinpath(pathlib.Path("Testdata"))
        p_str = str(p_pl)
        
        f_pl = pathlib.Path("test_file.dat")
        f_str = str(f_pl)
        
        tests = [
# path and filename are pathlib or string, output as pathlib
{"path": p_pl, "filename": f_pl, "extension": None, "string_out": False},
{"path": p_str, "filename": f_pl, "extension": None, "string_out": False},
{"path": p_pl, "filename": f_str, "extension": None, "string_out": False},
{"path": p_str, "filename": f_str, "extension": None, "string_out": False},
# path and filename are pathlib or string, output as string
{"path": p_pl, "filename": f_pl, "extension": None, "string_out": True},
{"path": p_str, "filename": f_pl, "extension": None, "string_out": True},
{"path": p_pl, "filename": f_str, "extension": None, "string_out": True},
{"path": p_str, "filename": f_str, "extension": None, "string_out": True},
# path and filename are pathlib or string, output as string
{"path": p_pl, "filename": f_pl, "extension": "dat", "string_out": True},
{"path": p_pl, "filename": f_pl, "extension": "csv", "string_out": True},
{"path": p_pl, "filename": f_pl, "extension": pathlib.Path(".csv"), "string_out": True},
        ]
        
        
        for t in tests:
            paf = CF.make_path_and_filename(path = t["path"], filename = t["filename"], extension = t["extension"], string_out = t["string_out"])
            s = "{:} {:} {:} {:}".format(t["path"], t["filename"], t["extension"], t["string_out"])
            with self.subTest(s): 
                self.assertTrue((type(paf) == str) == t["string_out"])
                print(paf)


        
        
if __name__ == '__main__': 
    verbosity = 1
    
    
    if 1:
        suite = unittest.TestLoader().loadTestsFromTestCase( Test_make_path_and_filename)
        unittest.TextTestRunner(verbosity=verbosity).run(suite)