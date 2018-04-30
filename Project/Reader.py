import csv
class Reader:
    """ Reads each csv file provided with the project brief. Returns the information in the form of a dictionary. """
    
    @staticmethod   
    def airport_reader():
        """ Creates a dictionary to store airports data """
        airports = {}
        with open('data/airport.csv', 'r', newline='', encoding='utf-8') as f:
            reader=csv.reader(f)
            for row in reader:
                ID = row[0]
                airport_name = row[1]
                city = row[2]
                country = row[3]
                airport_code = row[4]
                lat = float(row[6])
                lng = float(row[7])
                airport_altitude = int(row[8])
                region = row[11]
                    
                try:
                    airport_info = [airport_code,airport_name,lat,lng,city,country,region,airport_altitude]
                    airports[airport_code]=airport_info
                except ValueError:
                    row = [i.replace("\\", "") for i in row ]
        return airports
    
    @staticmethod 
    def aircraft_reader():
        """ Creates a dictionary to store aircrafts data. Converts imperial unuts to metric """
        aircrafts={}
        with open('data/aircraft.csv', 'r', newline='', encoding='utf-8') as f:
            reader=csv.reader(f)
            next(reader, None) 
            for row in reader:        
                code = row[0]
                type = row[1]
                manufacturer = row[3]
                units = row[2]
                if units == "imperial": # convert imperial to metric
                    range = float(row[4]) * 1.6093
                else:
                    range = float(row[4])
                aircraft_info = [code,range,type,manufacturer]
                aircrafts[code] = [aircraft_info]
        return aircrafts
    
    @staticmethod 
    def country_currency_reader():
        """ Creates a dictionary to store country currency data """
        currencies={}
        with open('data/countrycurrency.csv', 'r', newline='', encoding='utf-8') as f:
            reader=csv.reader(f)
            for row in reader:
                country_name = row[0]
                country_code = row[2]
                country_currency = row[14]
                country_info = [country_name,country_code,country_currency]
                currencies[country_name] = [country_info]
        return currencies
    
    @staticmethod 
    def currency_rates_reader():
        """ Creates a dictionary to store currency exchange rates data """
        rates={}
        with open('data/currencyrates.csv', 'r', newline='', encoding='utf-8') as f:
            reader=csv.reader(f)
            for row in reader:
                currency_name = row[0]
                currency_code = row[1]
                value_1 = row[2]
                value_2 = row[3]
                currency_info = [currency_name,currency_code,value_1,value_2]
                rates[currency_code] = [currency_info]
        return rates
    

