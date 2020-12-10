import networkx as nx

#show set of vertercies
def V(graph):
    return set(graph.nodes())
#show set of edges
def E(graph):
    return set(graph.nodes())
#creat graph
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
    return G[e[0]][e[1]]['weight']

#merging/union edges that is duplicated
def possible_edges(G, T):
    incidentedges=[]
    for e in G.edges():
        for v in T.nodes():
            if v in e:
                incidentedges.append(e)
            
    validedges=[]                      
    for e in incidentedges:
        if e[0] not in T.nodes() \
        or e[1] not in T.nodes():
            validedges.append(e)            
            
    return validedges
#sort() // temp_edge.sort() = (44:47)
#return lowest weight edge
def min_cost_edge(G, T):
    temp_edges = possible_edges(G, T)
    min_edge = temp_edges[0]
    for e in temp_edges:
        if (cost(G, e) < cost(G, min_edge)):
            min_edge=e
    return min_edge