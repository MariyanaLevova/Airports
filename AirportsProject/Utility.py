from math import pi,sin,cos,acos
import collections
import math
import networkx as nx
import matplotlib.pyplot as plt
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

class Graph:
    """ Class to create a graph object """
    
    def __init__(self):
        self.vertices = set()
        self.edges = collections.defaultdict(list)
        self.weights = {}
    
    def add_vertex(self,value):
        self.vertices.add(value)
        
    def add_edge(self, from_vertex, to_vertex, distance):
        if from_vertex == to_vertex:
            pass
        self.edges[from_vertex].append(to_vertex)
        #self.edges[to_vertex].append(from_vertex)
        self.weights[(from_vertex, to_vertex)] = distance
        #self.weights[(to_vertex, from_vertex)] = distance
        
    def __str__(self):
        string = 'Vertices: ' + str(self.vertices) + "\n"
        string += "Edges: " + str(self.edges) + "\n"
        string += "Weights: " + str(self.weights)
        return string
    
def dijkstra(graph,start):
    S = set()
    
    delta = dict.fromkeys(list(graph.vertices),99999)
    previous = dict.fromkeys(list(graph.vertices),None)
    delta[start]=0
    
    while S!= graph.vertices:
        
        v = min((set(delta.keys()) - S), key=delta.get)
        
        for neighbour in set(graph.edges[v])-S:
            new_path = delta[v] + graph.weights[v,neighbour]
            
            if new_path < delta[neighbour]:
                delta[neighbour]=new_path
                
                previous[neighbour] = v
                
        S.add(v)
    return (delta,previous)
        
        
def shortest_path(graph, start, end):
    """ Function that displays the shortest path between two nodes in a given graph
    
    Utilizes Dijkstra's algorithm
    """
    
    delta,previous = dijkstra(graph,start)
    
    path = []
    vertex = end
    
    while vertex is not None:
        path.append(vertex)
        vertex = previous[vertex]
        
    path.reverse()
    return path


# source https://networkx.github.io/documentation/stable/auto_examples/drawing/plot_directed.html
def draw_graph(graph, labels=None, graph_layout='spring',
               node_size=1200, node_color='blue', node_alpha=0.3,
               node_text_size=12,
               edge_color='blue', edge_alpha=0.3, edge_tickness=1,
               edge_text_pos=0.3,
               text_font='sans-serif'):
    
    """ Function to plot a valid itinerary graph """

    G=nx.DiGraph()

    # add edges
    for edge in graph:
        G.add_edge(edge[0], edge[1])

    graph_pos=nx.spring_layout(G)

    # draw graph
    nx.draw_networkx_nodes(G,graph_pos,node_size=[2000,node_size,node_size,node_size,node_size], 
                           alpha=node_alpha, node_color=["red","blue","blue","blue","blue"])
    nx.draw_networkx_edges(G, graph_pos, node_size=node_size, arrowstyle='->',
                               arrowsize=10, edge_color=edge_color,
                                width=2)
    nx.draw_networkx_labels(G, graph_pos,font_size=node_text_size,
                            font_family=text_font)

    if labels is None:
        labels = range(len(graph))

    edge_labels = dict(zip(graph, labels))
    nx.draw_networkx_edge_labels(G, graph_pos, edge_labels=edge_labels, 
                                 label_pos=edge_text_pos)

    # show graph
    plt.show()
