from Project.Aircraft import Aircraft
from Project.Airport import Airport
from Project.Utility import shortest_path as sp
from Project.Color import *
from Project.Utility import *
import csv
from numpy import empty
from _overlapped import NULL


def compute(array):
    """ Function to carry out all necessary calculations for the most efficient route """
    global feasible
    feasible = True
    aircraft = Aircraft(str(array[-1])) # creates an aircraft object based on the value of the last item in the input array
    print("List of desired destinations",Color.BLUE,array,Color.END) # prints the input array
    
    airports = [] # an empty array to store every airport object
    for i in range(len(array)-1):
        airport = Airport(array[i]) # creates an airport object for each element in the input array, except for the last element (the aircraft)
        airports.append([airport.code,airport.lat,airport.lng,airport.currency,float(airport.rate)])  

    distances = [] # an array to store the distances for each possible trip
    for i in airports:
        for j in airports:
            if i!=j:
                distance = round(distanceBetweenAirports(i[1],i[2],j[1],j[2]))
                adj_cost = float(i[4])*distance
                distances.append([i[0],j[0],distance,round(adj_cost)])

    itinerary = Graph() # creating a new graph object 
    for i in airports:
        itinerary.add_vertex(i[0]) # each airport is a node
    for i in distances:
        itinerary.add_edge(i[0], i[1], round(i[-1])) # each distance (considering the currency cost) is an edge (rounding the weight of the edges)
      
    shortest_paths = [] # an array to store the shortest path from each node to every other node
    for i in airports:
        for j in airports:
            if i!=j:
                shortest_paths.append(sp(itinerary,i[0],j[0])) # sp is shortest path using dijkstra's algo 
        
    for i in range(len(shortest_paths)):   
        cost = 0
        for j in range(len(shortest_paths[i])-1):
            cost += itinerary.weights[shortest_paths[i][j],shortest_paths[i][j+1]]
        shortest_paths[i].append(cost)
     
    tracker = [] # an array to store all visited airports
    origin = shortest_paths[0][0] # the origin airport is added to the tracker
    tracker.append(origin)
    
    graph = []
    dist = []
        
    def routing_algorithm(current):
        """ Function to find the nearest reachable airport that has not yet been added to the tracker """
        options = [] # an array to hold each viable route
        for i in range(len(shortest_paths)): 
            if distances[i][2] > aircraft.range: # checks if plane can fly that far
                continue
            elif shortest_paths[i][-2] in tracker: #checks if airport has been visited
                continue
            elif shortest_paths[i][0] != current: # checks that we're considering current airport as start off
                continue
            else:
                options.append(shortest_paths[i])                
        if options:
            options = sorted(options, key=lambda x: x[-1]) # sorts the options by distance
            next = options[0][-2]
        else:
            next = tracker[-1]
        tracker.append(next) # adds the next airport to the visited list
        return next
                  
    def print_itinerary():
        """ Prints the itinerary """
        for i in range(len(airports)-1):
            next = routing_algorithm(tracker[i])
        for i in range(len(tracker)):
            for j in range(i+1,len(tracker)):
                if tracker[i] == tracker[j]:
                    print()
                    print(Color.RED+"One or more of your destinations could not be reached.\nHere is the best possible route under these circumstances:"+Color.END)
                    tracker.pop(j)
                    global feasible
                    feasible = False
        return ""
    
    print(print_itinerary())
    tracker.append(origin)
    print("Optimal path", Color.BLUE,tracker,Color.END)
    print()
    print(Color.RED+"Trip Breakdown for each leg:"+Color.END)
    total_cost = 0
    for j in range(len(tracker)-1): 
        for i in distances:
            if i[0]==tracker[j] and i[1]==tracker[j+1]:
                print(i[0],"->",i[1],"Distance:",i[2],"Cost:",i[3])
                new = (i[0],i[1])
                graph.append(new)
                dist.append(i[3])
                total_cost += i[3]
    print()
    print("The total cost of this journey is:",Color.RED,total_cost,Color.END) 
    print() 

    edges = dist            
    
    if feasible:
        yes = (Color.RED,'I',  u'\u2764',"", u'\u2708',Color.END)
        print("This route IS feasible",*yes)
        with open(output_file, 'a', newline='') as a:
            writer = csv.writer(a)
            writer.writerow([array,tracker,total_cost])
        return graph, edges
        
    else:
        no = (Color.RED+u'\u2718'+Color.END)
        print(Color.RED+"PLEASE NOTE:"+Color.END)
        print("This route IS NOT feasible",no)
        with open(output_file, 'a', newline='') as w:
            writer = csv.writer(w)
            writer.writerow([array,"","NOT FEASIBLE"])
        return None, None
        
    
def main():
    """ Creates an array to store data input """
    try:
        input_file = input("Enter a file path for input: ")
        global output_file
        output_file = input("Enter a file path for output: ")
        print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
    
        with open(output_file, 'w', newline='') as w:
            writer = csv.writer(w)
            writer.writerow(["Original Input","Optimal Path","Cost/Conclusion"])
    
        with open(input_file, 'r', newline='', encoding='utf-8') as r:
            reader=csv.reader(r,dialect=csv.excel)
            graphs = []
            labelss = []
        
            for row in reader:
                ok_to_proceed = check_row(row)
                if ok_to_proceed:
                    graph, edges = compute(row)
                    graphs.append(graph)
                    labelss.append(edges)
                    print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
                else:
                    print("Invalid input",row)
                    print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
            for i in range(len(graphs)):
                if graphs[i] != None:
                    draw_graph(graphs[i], labelss[i])
            
        return ""
    except FileNotFoundError:
        print("The input file you entered does not seem to exist. Please try again:")
        main()
    except PermissionError:
        print("Something seems to have gone wrong, please try again:")
        main()
        
main()