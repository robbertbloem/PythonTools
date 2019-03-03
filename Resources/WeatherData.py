"""

"""

import numpy
import datetime


class WeatherData():    

    def __init__(self, path, base_filename):
        self.path = path
        self.base_filename = base_filename
        self.load_data()
        
    def load_data(self):
        self.data = numpy.load(self.path + self.base_filename + "_data.npy")
        self.data = numpy.array(self.data, dtype = numpy.float64)
        self.codes = numpy.load(self.path + self.base_filename + "_codes.npy")
    
        

    def find_values_for_dates(self, datetimes, keys):

        vals = []

        dt = self.data[:,1:3]

        


        for i in range(len(datetimes)):
    
            v = [0] * len(keys)
            
    
            d = int(datetimes[i].strftime("%Y%m%d"))
            t = int("{:d}".format(datetimes[i].hour)) 
            idx = numpy.where(numpy.logical_and(dt[:,0] == d, dt[:,1] == t))[0][0]
            for k in range(len(keys)):
                v[k] = self.data[idx, keys[k]]
            
            vals.append(v)
            
        vals = numpy.array(vals)
        
        return vals
            
            
            
    def weather_for_dates_and_times(self, datetimes):

        vals = []

        dt = self.data[:,1:3]
        
        for i in range(len(datetimes)):

            d = int(datetimes[i].strftime("%Y%m%d"))
            t = int("{:d}".format(datetimes[i].hour)) 
            idx = numpy.where(numpy.logical_and(dt[:,0] == d, dt[:,1] == t))[0][0]
            vals.append(self.data[idx,:])
            
        vals = numpy.array(vals)
        
        return vals            
        

    def correct_data(self, data = 0):
        if type(data) == int:
            data = self.data[:,:]
        
        var_DD = []
        
        for i in range(len(self.codes)):

            
   
            if self.codes[i] == "DD": # windrichting
                var_DD = numpy.where(data[:,i] > 360)[0]
                

            elif self.codes[i] == "FH": # uurgemiddelde windsnelheid
                data[:,i] *= 0.36   
                data[var_DD,i] = 0

                
                
        return data





if __name__ == "__main__": 

    path = "/Users/robbert/Transporter/Developer/Languages/Python/Weather/"
    filename = "weather_data.npy"
    
    weather = WeatherData(path + filename)
    
    datetimes = [datetime.datetime(2017, 5, 15, 7, 44), datetime.datetime(2017, 5, 16, 17, 44), datetime.datetime(2017, 5, 17, 17, 44), datetime.datetime(2017, 5, 16, 7, 44)]
    keys = [3,4]
    

    vals = weather.find_values_for_dates(datetimes, keys)
    
    for i in range(4):
        print(datetimes[i], vals[i])
    
#     print(vals)
    