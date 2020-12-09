import networkx as nx

def V(graph):
    return set(graph.nodes())

def E(graph):
    return set(graph.edges())

def prims_initialize(graph, v):
    if v not in V(graph):
        return "Error vertex not found"
    T = nx.Graph()
    T.add_node(v)
    return T

def is_spanning(graph, subgraph):
    return V(graph) == V(subgraph)

def cost(G, e):
    return G[e[0]][e[1]]['weight']

def possible_edges(G, T):
    return [e for e in list(G.edges(V(T)))
             if e[0] not in V(T) or e[1] not in V(T)]

def min_prims_edge(G, T):
            