from __future__ import print_function
from __future__ import division
from __future__ import absolute_import
from __future__ import unicode_literals

import inspect
import shelve
import os

import PythonTools.ClassTools as CT


class objectarray(CT.ClassTools):
    """
    object array class - functions for arrays of objects
    
    
    
    
    """
    
    
    
    
    def __init__(self, name = "name", obj_id = "objectarray", flag_verbose = False):
        """
        Initialize an object array.
        
        INPUT:
        - name (string, 'name'): a name
        - obj_id (string, 'objectarray'): the object id
        
        OUTPUT:
        obj_array is initialized. The object array contains the objects
        
        CHANGELOG:
        20130131/RB: started class in Crocodile
        20130201/RB: moved class to PythonTools
        20130201/RB: replaced self.obj_id_array by a property with the same name. One less thing to keep track of, same results.
        
        """
        self.verbose("Created object array", flag_verbose)
        
        self.obj_id = obj_id    # identifier
        self.name = name        # name - optional       
        self.obj_array = []     # array with objects


    @property
    def obj_id_array(self):
        """
        returns an array with only object id's
        
        CHANGELOG:
        20130201/RB: started function. No need to keep track of an extra variable.        
        """ 
        obj_id_array = []
        for obj in self.obj_array:
            obj_id_array.append(obj.obj_id) 
        return obj_id_array

    # phase   
    @property
    def obj(self):
        return self.obj_array




    def add_object(self, obj, flag_verbose = False):
        """
        Add an object to the array
        
        INPUT:
        - obj: an object, containting at least an obj_id. It is useful to have a sub_type, but not required.
        
        OUTPUT:
        - BOOL, True when okay, False for failure
        
        CHANGELOG:
        20130131/RB: started function
        
        """
        self.verbose("Add object", flag_verbose)
        
        try:
            # test if object-id is unique
            if obj.obj_id in self.obj_id_array:
                self.printError("obj_id already exists, will not add new object.", inspect.stack())
                return False
        except AttributeError:
            self.printError("Object should have an obj_id", inspect.stack())
            return False            
            
        self.verbose("  new object is appended.", flag_verbose)
        self.obj_array.append(obj)
        return True


    def add_array_with_objects(self, obj_array, flag_verbose = False):
        """
        Add an array of objects to the array
        
        INPUT:
        - obj_array: an array with objects, each containting at least an obj_id. It is useful to have a sub_type, but not required.
        
        OUTPUT:
        - BOOL, True when okay, False for failure
        
        CHANGELOG:
        20130208/RB: started function
        
        """       
        
        self.verbose("Add object array", flag_verbose)
        
        for obj in obj_array:
            self.add_object(obj, flag_verbose = flag_verbose)





    def save_objectarray(self, path_and_filename, flag_overwrite = False, flag_verbose = False):
        """
        Save the array as a pickle
        
        INPUT:
        - path_and_filename (string): path and filename of pickle
        - flag_overwrite (BOOL, False): if True, then the file is overwritten
        
        OUTPUT:
        - True
        
        CHANGELOG:
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
            db[str(object.obj_id)] = object
        db.close()
        os.system("chmod 777 " + path_and_filename)
        
        return True

        
    def import_db(self, path_and_filename, flag_verbose = False):
        """
        Imports a database. The function checks for the existence of the database. It returns "False" if the file doesn't exist. Otherwise, it will return an array with class instances.
        The order of the objects is random. Use 'load_objectarray' to import with an order (requires an obj_id_array).
        
        INPUT:
        - path_and_filename (string): path and filename of pickle
        
        OUTPUT:
        - True for succes, False for failure
        - obj_array is populated
        
        CHANGELOG:
        20130131/RB: copied function from croc
        
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
        
        OUTPUT:
        - True for success, False for Failure
        - obj_array is populated
                
        CHANGELOG
        20130201/RB: started function. Origin is in import_db and croc.Pe
              
        BEHAVIOR:
        For a pickle with objects a, b and c, a given obj_id_array_in will result in an obj_array which contains
        obj_id_array_in   result
        a b c           = a b c
        a b             = a b
        a b c d         = a b c
        a b d           = a b
        
        """
        
        if path_and_filename[-7:] != ".pickle":
            path_and_filename += ".pickle"
            self.verbose("  Added .pickle to path_and_filename", flag_verbose)
        
        if os.path.isfile(path_and_filename) == False:
            self.printError("The file doesn't exist!", inspect.stack())
            return False  
            
        db=shelve.open(path_and_filename)
        temp_array = []
        for key in db:
            if flag_verbose:
                self.verbose(key, flag_verbose)
            temp_array.append(db[key])
        db.close() 
        
        # make the new arrays
        self.obj_array = [] 
        
        for i in range(len(obj_id_array_in)):
            for j in range(len(temp_array)):              
                if obj_id_array_in[i] == temp_array[j].obj_id:
                    self.obj_array.append(temp_array[j])

        return True


    def print_objects(self, index = -1, flag_verbose = False):
        """
        Print the objects of the array. This will print all the details of the objects.
        
        INPUT:
        None
        
        OUTPUT:
        Function prints the details of all objects
        
        CHANGELOG:
        20130131/RB: started function
        20130208/RB: introduced index to print only one element
        
        """
        self.verbose("Print objects", flag_verbose)
        if index > len(self.obj_array) - 1:
            self.printError("Index is out of bounds.", inspect.stack())
        elif index > -1:
            print(self.obj_array[index])
        else:
            for i in self.obj_array:
                print(i)


    def print_object_ids(self, flag_verbose = False):
        """
        Print the objects of the array. This will only print the object ids.
        
        INPUT:
        None
        
        OUTPUT:
        Function prints the object ids as strings.
        
        CHANGELOG:
        20130131/RB: started the function
        20130208/RB: if object has variable 'sub_type' it will print that as well. Made the printing look nicer. 
        
        """
        self.verbose("Print object ids", flag_verbose)
        print("id's for objects in object array " + self.name)
        for i in range(len(self.obj_array)):
            if hasattr(self.obj_array[i], "sub_type"):
                print("{0:3d} {1:10s} {2:10s}".format(i, self.obj_array[i].obj_id, self.obj_array[i].sub_type))
            else:
                print("{0:3d} {1:10s}".format(i, self.obj_array[i].obj_id))


    def list_objects_with_sub_type(self, sub_type, flag_verbose = False):
        """
        Return an array with the indices of objects that have a certain sub_type. 
        
        INPUT:
        - sub_type (string): string of sub_type
        
        OUTPUT:
        - a list with indices of obj_array with the given sub_type
        
        CHANGELOG:
        20130201/RB: started the function
        20130211/RB: instead of string, you can now also give an array with string
        
        """
        if type(sub_type) != list:
            sub_type = [sub_type]
            
        sub_type_array = []
        
        for i in range(len(self.obj_array)):
            if self.obj_array[i].sub_type in sub_type:
                sub_type_array.append(i) 
        
        if len(sub_type_array) == 0:
            self.printWarning("sub_type_array is empty", inspect.stack())
            
        return sub_type_array


    def objects_with_sub_type(self, sub_type, flag_verbose = False):

        if type(sub_type) != list:
            sub_type = [sub_type]
                
        sub_type_array = []
        
        for idx in self.obj_array:
            if idx.sub_type in sub_type:
                sub_type_array.append(idx) 
        
        if len(sub_type_array) == 0:
            self.printWarning("sub_type_array is empty", inspect.stack())
            
        return sub_type_array        



    def objects_from_list(self, list_with_indices, flag_verbose = False):
        
        new_list = []
        
        for idx in list_with_indices:
            new_list.append(self.obj_array[idx])
            
        return new_list
        
        
        


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
