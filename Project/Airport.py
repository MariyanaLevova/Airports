import Project.Reader as reader
from Project.Color import Color as color

airports = reader.Reader.airport_reader()
country_currency = reader.Reader.country_currency_reader()
rates = reader.Reader.currency_rates_reader()

class Airport:
    
    def __init__(self, code):
        self.code = code
        self.name = airports[code][1]
        self.lat = float(airports[code][2])
        self.lng = float(airports[code][3])
        self.city = airports[code][4]
        self.country = airports[code][5]
        self.region = airports[code][6]
        self.altitude = airports[code][7]
        self.currency = country_currency[self.country][0][2]
        self.rate = rates[self.currency][0][2]
        
        
    def __repr__(self):
        return "Airport is " + self.name + " in " + self.country + " currency " + self.currency + " exchange rate is " + self.rate + " Coordinates: " + str(self.lat) + " " + str(self.lng)
