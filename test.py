"""
import networkx as nx
from functions import *
from algorithms import prims_algorithm
from drawing import *

graph_data = open('test_graph/G1.txt','r')
G = nx.read_weighted_edgelist(graph_data, nodetype = int)
T = prims_init(G, 0, show_graph = True, show_cost = True)

"""