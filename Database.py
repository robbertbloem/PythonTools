from __future__ import print_function
from __future__ import division
from __future__ import absolute_import

import sqlite3

import numpy
import matplotlib 
import matplotlib.pyplot as plt

import PythonTools.ClassTools as CT


class DB_functions(CT.ClassTools):
    
    def __init__(self, dbname, path):
    
        self.dbname = dbname
        self.path = path
        
        self.conn = sqlite3.connect(path)
        self.cursor = self.conn.cursor()
        
    def create_table(self, tablename, col_names, col_types = False):
        """
        
        INPUT:
        - tablename (string): name of the table to be created
        - col_names (list with strings): names of the columns in the table
        - col_types (False, or list with strings): types of the columns. If False (default) it will use default (text). 
        
        OUTPUT:
        None
        
        CHANGELOG:
        2015/9/17-RB: added documentation
        
        """

        s = "CREATE TABLE"
        s = "".join([s, " ", tablename, " ("])
        for c in range(len(col_names)):
            if col_types:
                s = "".join([s, " ", col_names[c], " ", col_types[c]])
            else:
                s = "".join([s, " ", col_names[c]])
            if c < len(col_names) - 1:
                s = "".join([s, ", "])  
        s = "".join([s, ")"])
        self.cursor.execute(s)
        
        
    def add_rows(self, tablename, rows):
        
        temp = ["INSERT INTO ", tablename, " VALUES ("] + ["?, "] * (len(rows[0]) - 1) + ["?)"]
        s = "".join(temp) 
        self.cursor.executemany(s, rows)
        

    def return_rows(self, tablename, columns):      
        s = "SELECT"  
        for c in range(len(columns)):
            s = "".join([s, " ", columns[c]])
            if c < len(columns) - 1:
                s = "".join([s, ","])  
        s = "".join([s, " FROM ", tablename])
        for row in self.cursor.execute(s):
            print(row)
#             
#     def query_to_int_array(self, query):
#         res = []
#         for row in self.cursor.execute(query):
#             res.append(int(row[0]))
#         return res
#     
#     def query_to_int_nparray(self, query):
#         res = numpy.array([])
#         for row in self.cursor.execute(query):
#             res = numpy.append(res, [row[0]])
#         return res
#     
#     def query(self, query):
#         res = []
#         for row in self.cursor.execute(query):
#             res.append(row)
#         return res
# 
#     def query_wijkcodes(self, tablename, exclude_expat = True):
#         query = "SELECT wijkcode FROM %s" % tablename
#         temp = self.query_to_int_nparray(query)
#         temp = numpy.unique(temp)
#         if exclude_expat and temp[-1] == 88:
#             temp = temp[:-1]
#         
#         return temp
# 
# 
#     def commit(self):
#         self.conn.commit()
# 
#     def close(self):
#         self.conn.close()
# 

    

        
        
if __name__ == "__main__": 
    
    
    
    
    x = DB_functions("Database", ":memory:")
    
    tablename = "verkiezingen"

    col_names = ["verkiezing", "jaar"] #, "wijk", "partij", "stemmen"]
    col_types = ["text", "integer"]
    
    x.create_table(tablename, col_names, col_types)
    
    rows =  [("TK", 2010), ("TK", 2012)] 
    #[("TK", "2010", "A", "D66", "100"), ("TK", "2012", "B", "D66", "200")] 
#     
    x.add_rows(tablename, rows)
    
    y = x.return_rows(tablename, ["jaar"])
    print(y)
