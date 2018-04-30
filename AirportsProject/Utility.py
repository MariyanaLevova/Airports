from math import pi,sin,cos,acos
import collections
import math

import Reader as reader

airports = reader.Reader.airport_reader()
aircraft = reader.Reader.aircraft_reader()
    
def distanceBetweenAirports(latitude1, longitude1, latitude2, longitude2):
    """ Calculates the distance between two points given their coordinates """
    
    radius_earth = 6371 # in kms
    theta1 = longitude1 * (2 * pi) / 360
    theta2 = longitude2 * (2 * pi) / 360
    phi1 = (90 - latitude1) * (2 * pi) / 360
    phi2 = (90 - latitude2) * (2 * pi) / 360
    distance = acos(sin(phi1)*sin(phi2)*cos(theta1-theta2)+cos(phi1)*cos(phi2))*radius_earth
    return distance

def check_row(row):
    """ Ensures the program input follows the rules outlined below """
    yes = True
    no = False
    if len(row) != len(set(row)): # checks for duplicate items in the airport list 
        return no
    elif len(row) != 6:
        return no
    elif [x for x in row[0:-1] if x not in airports]: #checks if each airport exist
        print("One or more of the airport entries is not recognised.")
        return no 
    elif row[-1] not in aircraft: # checks if the aircraft exists
        print("The aircraft code is not recognised.")
        return no
    else:
        return yes

