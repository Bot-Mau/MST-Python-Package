import networkx as nx
from functions import *
from drawing import show_weighted_graph, draw_subtree


def prims_algorithm(G, starting_vertex, show_graph = False, show_cost = False):
   #The function reads the graph G and uses starting_vertex to run prim's algorithm
   #it will create a temp graph T which is a copy of the main graph. 
   #In the loop, T will be compare with G to check if T has already as big as G
   #if T is not, then the function will add the minimum and possible edge from G to T.
   #after the loop, the function will calculate all the edge in the graph if the user wish to see its cost
   #the return value is the graph T
   if show_graph == True:
       show_weighted_graph(G)
   #create temp graph
   T = prims_init(G, starting_vertex)
   #draw T graph
   if show_graph == True:
       draw_subtree(G, T)
    
   while is_spanning(G, T) == False:
       e = min_cost_edge(G, T)
       T.add_edge(e[0], e[1], weight = cost(G, e))
       if show_graph == True:
           draw_subtree(G, T)
   #show cost
   if show_cost == True:
        c = sum(cost(G, e) for e in T.edges())
        print(f'The cost of this spanning tree is {c}')
   return T
