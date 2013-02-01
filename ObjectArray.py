from __future__ import print_function
from __future__ import division

import inspect
import shelve
import os

import PythonTools.ClassTools as CT


class objectarray(CT.ClassTools):
    
    def __init__(self, name = "name", obj_id = "objectarray", flag_verbose = False):
        
        self.verbose("Created object array", flag_verbose)
        
        self.obj_id = obj_id    # identifier
        
        self.name = name        # name - optional
        
        self.obj_array = []     # array with objects
        self.obj_id_array = []  # array with object-identifiers, to prevent duplicates. The array is not necesarily in the correct order.



    def add_object(self, obj, flag_verbose = False):
        """
        Add an object to the array
        
        """
    
        self.verbose("Add object", flag_verbose)
        
        # test if object-id is unique
        if obj.obj_id in self.obj_id_array:
            self.printError("obj_id already exists, will not add new object.", inspect.stack())
            return False
        
        self.verbose("  new object is appended.", flag_verbose)
        self.obj_array.append(obj)
        self.obj_id_array.append(obj.obj_id)
        return True
         
        

    def save_objectarray(self, path_and_filename, flag_overwrite = False, flag_verbose = False):
        """
        Save the array
        """

        self.verbose("Save object array", flag_verbose)

        # check filename
        if path_and_filename[-7:] != ".pickle":
            path_and_filename += ".pickle"
            self.verbose("  Added .pickle to path_and_filename", flag_verbose)
        
        # check if you want to overwrite it
        if flag_overwrite:
            self.printWarning("make_db: overwrite flag is True", inspect.stack())
            flag_overwrite = "n"
        else:
            flag_overwrite = "c"  

        # save it
        db = shelve.open(path_and_filename, flag = flag_overwrite)
        for object in self.obj_array:
            db[object.obj_id] = object
        db.close()
        os.system("chmod 777 " + path_and_filename)
        
        return True

        
    def import_db(self, path_and_filename, flag_verbose = False):
        """
        Imports a database. The function checks for the existence of the database. It returns "False" if the file doesn't exist. Otherwise, it will return an array with class instances.
        The order of the objects is random. Use 'load_objectarray' to import with an order (requires an obj_id_array).
        """
        
        if path_and_filename[-7:] != ".pickle":
            path_and_filename += ".pickle"
            self.verbose("  Added .pickle to path_and_filename", flag_verbose)
     
        if os.path.isfile(path_and_filename) == True:
            db=shelve.open(path_and_filename)
            obj_array = []
            for key in db:
                if flag_verbose:
                    self.verbose(key, flag_verbose)
                self.obj_array.append(db[key])
                self.obj_id_array.append(db[key].obj_id)
            db.close() 
            return True
        else:     
            self.printError("The file doesn't exist!", inspect.stack())
            return False
    
    
    
    def load_objectarray(self, path_and_filename, obj_id_array_in, flag_verbose = False):
        """
        Load object array: import a pickle with the order of obj_id_array_in
        
        INPUT:
        - path_and_filename (string): path and filename of the pickle
        - obj_id_array_in (list): object ids to be loaded (see behavior for details)
        
        CHANGELOG
        20130201/RB: started function. Origin is in import_db and croc.Pe
              
        BEHAVIOR:
        For a pickle with objects a, b and c, a given obj_id_array_in will result in an obj_array which contains
        obj_id_array_in   result
        a b c           = a b c
        a b             = a b
        a b c d         = a b c
        a b d           = a b
        
        NOTE:
        Test case is available
        
        """
        
        if path_and_filename[-7:] != ".pickle":
            path_and_filename += ".pickle"
            self.verbose("  Added .pickle to path_and_filename", flag_verbose)
        
        if os.path.isfile(path_and_filename) == False:
            self.printError("The file doesn't exist!", inspect.stack())
            return False  
            
        db=shelve.open(path_and_filename)
        temp_array = []
        temp_id_array = []
        for key in db:
            if flag_verbose:
                self.verbose(key, flag_verbose)
            temp_array.append(db[key])
            temp_id_array.append(db[key].obj_id) 
        db.close() 
        
        # make the new arrays
        self.obj_array = [] #* len(obj_id_array_in)
        self.obj_id_array = [] #* len(obj_id_array_in)
        
        for i in range(len(obj_id_array_in)):
            for j in range(len(temp_array)):              
                if obj_id_array_in[i] == temp_array[j].obj_id:
                    self.obj_array.append(temp_array[j])
                    self.obj_id_array.append(self.obj_array[i].obj_id)

        return True


    def print_objects(self, flag_verbose = False):
        """
        Print the objects of the array. This will print all the details of the objects.
        """
        self.verbose("Print objects", flag_verbose)
        for i in self.obj_array:
            print(i)

    def print_object_ids(self, flag_verbose = False):
        """
        Print the objects of the array. This will only print the object ids.
        """
        self.verbose("Print object ids", flag_verbose)
        for i in self.obj_id_array:
            print(i)


    def object_with_sub_type(self, sub_type, flag_verbose = False):
        """
        Return an array with the indices of objects that have a certain sub_type. 
        """
        sub_type_array = []
        
        
        
        for i in range(len(self.obj_array)):
            if self.obj_array[i].sub_type == sub_type:
                sub_type_array.append(i) 
        
        if len(sub_type_array) == 0:
            self.printWarning("sub_type_array is empty", inspect.stack())
            
        return sub_type_array



class testobject(CT.ClassTools):
    """
    Lightweight object to test the tools with.
    
    CHANGELOG:
    20130131/RB: started
    
    """
    
    def __init__(self, name, obj_id, sub_type = "", flag_verbose = False):
        
        self.verbose("Create test object", flag_verbose)     
        self.name = name
        self.obj_id = obj_id
        self.sub_type = sub_type
        
        self.variable = 0




if __name__ == "__main__": 

    pass
