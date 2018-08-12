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
                row["Gemiddelde snelheid"] = float(row["Gemiddelde snelheid"].replace(",", "."))
        
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
                row["Datum"] = datetime.date(y, m, d)
        
            if "Gem. HS" in row:
                row["Gem. HS"] = int(row["Gem. HS"])
                
        return data



if __name__ == "__main__": 

    path = "/Users/robbert/Transporter/Developer/Languages/Python/garmin/"
    paf = path + "Activities_total.csv"
    
    
    fiets = CSVReader(paf)
    data = fiets.read_csv()
    data = data[::-1]    
    data = fiets.clean_garmin_data(data)
    

    

    