"""

"""

import csv
import datetime

import numpy




class CSVReader():
    
    def __init__(self, paf):
        self.paf = paf

     
    def read_csv(self):
        
        csv.register_dialect("skipspace", delimiter = ",", skipinitialspace = True)
        
        with open(self.paf) as csvfile:
            reader = csv.DictReader(csvfile, dialect = "skipspace")
            
            data = []
            for row in reader:
                data.append(dict(row))
                
        return data



    def clean_garmin_data(self, data):
    
        data = [x for x in data if ("Fietsen" or "Cycling") in x["Titel"]]
    
        for row in data:
 
            if "Afstand" in row:    
                row["Afstand"] = float(row["Afstand"].replace(",", "."))
                
            if "Gemiddelde snelheid" in row:
                row["Gemiddelde snelheid"] = numpy.float64(row["Gemiddelde snelheid"].replace(",", "."))
        
            if "Tijd" in row:
                temp = row["Tijd"]
                if "," in temp:
                    temp = temp[:-2]
                s = int(temp[-2:])
                m = int(temp[-5:-3])

                row["Tijd"] = datetime.timedelta(minutes = m, seconds = s)

            if "Datum" in row:
                temp = row["Datum"]
                y = int(temp[:4])
                m = int(temp[5:7])
                d = int(temp[8:10])
                h = int(temp[11:13])
                mi = int(temp[14:16])
                s = int(temp[17:19])
                row["Datum"] = datetime.datetime(y, m, d, h, mi, s)
        
            if "Gem. HS" in row:
                row["Gem. HS"] = int(row["Gem. HS"])
                
        return data



    def select_data_distance(self, data, distance, delta_d):
        
        data = [x for x in data if x["Afstand"] > distance - delta_d]
        data = [x for x in data if x["Afstand"] < distance + delta_d]
        
        return data
        
    def select_and_split_from_title(self, data, names):

        _data = [0] * len(names)
        
        for i in range(len(names)):
            _data[i] = [x for x in data if names[i] in x["Titel"]]
    
        return _data





    def extract_values(self, data, keys):
        """
        Collect the values for particular keys for every activity. 
        The date is not automatically included. 
        """
        values = [0] * len(data)
        
        for r in range(len(data)):
            v = numpy.array((3), dtype = numpy.float64)
            v = [0] * (len(keys))
            for k in range(len(keys)):
                v[k] = data[r][keys[k]]
            values[r] = v
               
        values = numpy.array(values)
        return values
        
        
    def moving_average(self, dates, values, n = 3):
        ret = numpy.cumsum(values, dtype=float)
        ret[n:] = ret[n:] - ret[:-n]
        ret = ret[n - 1:] / n   
        
        a = int(numpy.floor(n / 2))
        b = a + len(ret)
        dates = dates[a:b]
        
        return dates, ret


    def datetime_only_date(self, datetimes):
        dates = []
        for i in range(len(datetimes)):
            dates.append(datetimes[i].replace(hour = 0, minute = 0, second = 0))
        dates = numpy.array(dates)
        return dates
    
    def find_vals_same_date(self, vals1, vals2, date_col, val_col):
        """
        vals1 and vals2: arrays with values
        date_col: index of column with dates
        val_col: column of required value
        """
        new_vals = []

        dates1 = self.datetime_only_date(vals1[:,date_col])
        dates2 = self.datetime_only_date(vals2[:,date_col])
        
        for i in range(len(vals1)):
            v = [0,0,0]

            if dates1[i] in dates2:
                v[0] = dates1[i]
                v[1] = vals1[i, val_col]
                idx = numpy.where(dates1[i] == dates2)[0]
                v[2] = vals2[idx, val_col][0]
                new_vals.append(v)
        new_vals = numpy.array(new_vals)
        return new_vals
        
    



if __name__ == "__main__": 

    path = "/Users/robbert/Transporter/Developer/Languages/Python/garmin/"
    paf = path + "Activities_total.csv"
    
    
    fiets = CSVReader(paf)
    data = fiets.read_csv()
    data = data[::-1]    
    data = fiets.clean_garmin_data(data)
    

    

    