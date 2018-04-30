from Aircraft import *
from Airport import *
from Utility import *
from Graph import Graph as graph
from Graph import shortest_path as sp
from Color import *
from Reader import Reader as reader
import unittest


class TestAirports(unittest.TestCase):
    """ A class to test functions in this project """
    
    def test_aircraft(self):
        a = Aircraft("777")
        self.assertTrue(a.fuelLevel==0)
        self.assertTrue(a.range==15610)
        a.refuel(2000)
        self.assertTrue(a.fuelLevel==2000)
        b = Aircraft("A330")
        b.refuel_to_full(1)
        self.assertTrue(b.fuelLevel==13430)
        b.flight_distance(430)
        self.assertTrue(b.fuelLevel==13000)
        
    def test_airport(self):
        dub = Airport("DUB")
        self.assertTrue(dub.currency=="EUR")
        self.assertTrue(dub.name=="Dublin")
        self.assertTrue(dub.country=="Ireland")

    def test_distance(self):
        dub = Airport("DUB")
        lhr = Airport("LHR")
        dub_lat = dub.lat
        dub_lng = dub.lng
        lhr_lat = lhr.lat
        lhr_lng = lhr.lng
        distance = round(distanceBetweenAirports(dub_lat,dub_lng,lhr_lat,lhr_lng))
        self.assertTrue(distance==449)
        self.assertFalse(distance==5000)
         
    def test_graph(self):
        g = graph()
        airports = ["a","b","c"]
        for i in airports:
            g.add_vertex(i)
        for i in range(len(airports)):
            for j in range(len(airports)):
                if i != j:
                    g.add_edge(airports[i], airports[j], i+j)     
        self.assertTrue(g.weights["a","b"]==1)
        self.assertTrue(g.weights["b","c"]==3)

         
    def test_shortest_path(self):
        g = graph()
        airports = ["a","b","c"]
        for i in airports:
            g.add_vertex(i)
        for i in range(len(airports)):
            for j in range(len(airports)):
                if i != j:
                    g.add_edge(airports[i], airports[j], i+j) 
        self.assertTrue(sp(g,"a","b")==['a', 'b'])
        self.assertTrue(sp(g,"c","a")==['c', 'a'])
        self.assertFalse(sp(g,"c","b")==['c', 'a', 'b'])
        
    def test_reader(self):
        
        aircrafts = reader.Reader.aircraft_reader()
        a330 = aircrafts.get("A330")
        b_737 = aircrafts.get("737")
        b_777 = aircrafts.get("777")
        self.assertTrue(a330[0][3]=="Airbus")
        self.assertTrue(b_737[0][2]=="jet")
        self.assertTrue(b_777[0][1]<17000)
        
        airports = reader.Reader.airport_reader()
        auh = airports.get("AUH")
        self.assertTrue(auh[4]=="Abu Dhabi")
        
        country_currency = reader.Reader.country_currency_reader()
        ie = country_currency.get("Ireland")
        self.assertTrue(ie[0][2]=="EUR")
        
        rates = reader.Reader.currency_rates_reader()
        usd = rates.get("USD")
        self.assertTrue(usd[0][0]=="US Dollar")
        
    def test_check_row(self):
        row = ["DUB", "AUH", "LAX", "ORK", "MAN", "777"]
        row2 = ["DUB", "auh","AUH", "LAX", "ORK", "777"]
        self.assertTrue(check_row(row))
        self.assertTrue(check_row(row2))
        
    def test_color(self):
        print("hello")
        print(Color.GREEN+"hello"+Color.END)
        print(Color.CYAN+"hello"+Color.END)
        print(Color.DARKCYAN+"hello"+Color.END)
        print(Color.BLUE+"hello"+Color.END)
        print(Color.WARNING+"hello"+Color.END)
        print(Color.PURPLE+"hello"+Color.END)
        print(Color.RED+"hello"+Color.END)
        
        
if __name__ == "__main__":
    suite = unittest.defaultTestLoader.loadTestsFromTestCase(TestAirports)
    unittest.TextTestRunner().run(suite)
