import networkx as nx

#original graph
def V(graph):
    return set(graph.nodes())
#
def E(graph):
    return set(graph.nodes())
#create graph
def prims_init(graph, v):
    if v not in V(graph):
        return "Enter vertex not found"
    else: 
        T = nx.Graph()
        T.add_node(v)
        return T 
    
#check if the tree is equal to its subgraph
def is_spanning(graph, subgraph):
    return V(graph) == V(subgraph)

#return weight of the edge
def cost(G, e):
    return G[e[0]][e[1]]["weight"]

#merging/union edges that is duplicated
def possible_edges(G, T):
    return [e for e in list(G.edges(V(T)))
            if e[0] not in V(T) or e[1] not in V(T)]


#return lowest weight edge
def min_cost_edge(G, T):
    temp_edges = possible_edges(G, T) #return possible edges
    #comparing one edge to another by weight to get the smalles edge weight
    min_edge = temp_edges[0]
    for e in temp_edges:
        min_edge = e if  (cost(G, e) < cost(G, min_edge)) else min_edge
    return min_edge
