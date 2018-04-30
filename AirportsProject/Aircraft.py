import Reader as reader

aircraft = reader.Reader.aircraft_reader()

class Aircraft:
    """ A class to generate aircraft objects"""
    
    def __init__(self, IATA):
        self.IATA=IATA 
        self.range = round(aircraft[IATA][0][1])
        self.fuelLevel = 0
        self.maxFuel = self.range
        self.journey_cost = 0
        
    def fuelCheck(self):
        return self.fuelLevel
    
    def journey_cost(self):
        return self.journey_cost
    
    def range(self):
        return self.range
        
    def refuel(self, amount):
        self.fuelLevel += amount
        if self.fuelLevel > self.maxFuel:
            self.leftover = self.fuelLevel - self.maxFuel
            self.fuelLevel = self.maxFuel
            
            print("Excess fuel", self.leftover)

        
    def refuel_to_full(self,exchange_rate):
        to_full = self.maxFuel - self.fuelLevel
        self.refuel(to_full)
        self.cost = to_full*exchange_rate
        self.journey_cost +=self.cost
        print("Added",to_full,"litres with exchange rate",exchange_rate)
        print("Cost of last refuel",self.journey_cost)
        
    def flight_distance(self,distance):
        if self.range < distance:
            print("This aircraft cannot complete the journey. Aircraft range is",self.range)
            print("The requires distance is", distance)   
        else:
            self.fuelLevel -= distance 
        
    def __repr__(self):
        return "Aircraft code is " + self.IATA + " Aircraft range is " + str(self.range) 

