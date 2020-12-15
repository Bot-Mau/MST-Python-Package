import networkx as nx

def V(graph):
    #this function is used to return all nodes in the graph
    return set(graph.nodes())

def E(graph):
    #this function is same with V(graph), but it is used to avoid same definition of function
    #during comparision
    return set(graph.nodes())

def prims_init(graph, v):
    #This function adds node v into existing graph T. The return value is graph T after added node v
    if v not in V(graph):
        return "Enter vertex not found"
    else: 
        T = nx.Graph()
        T.add_node(v)
        return T 
    
def is_spanning(graph, subgraph):
    #this version compare 2 graph and return true if they are the same (size), otherwise, the fuction return false
    return V(graph) == V(subgraph)


def cost(G, e):
    #this function return weight of an edge e
    return G[e[0]][e[1]]["weight"]


def possible_edges(G, T):
    #this function returns all possible edges after union all duplicated edges
    return [e for e in list(G.edges(V(T)))
            if e[0] not in V(T) or e[1] not in V(T)]

def min_cost_edge(G, T):
    #the function return the smallest edge of the graph. the function calls possible_edge in order to
    #remove duplicated edge. Then the fuction will compare one edge to another using binary comparsion
    #and store smallest value in min_edge. it will return min_edge after the loop exterminates
    temp_edges = possible_edges(G, T) 
    #comparing one edge to another by weight to get the smalles edge weight
    min_edge = temp_edges[0]
    for e in temp_edges:
        min_edge = e if  (cost(G, e) < cost(G, min_edge)) else min_edge
    return min_edge
