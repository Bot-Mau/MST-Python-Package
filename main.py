import networkx as nx
from algorithms import prims_algorithm

val = input("Indicate (1) if you want to see example graph or (2) to input the graph: ")

if int(val) == 1:#example graph
    
    q = input("Show Cost (Y/N): ")
    showCost = True if not val=='Y' else False
    q = input("Show Graph (Y/N):")
    showGraph = True if not val=='Y' else False
    
    #read graph from file
    graph_data = open('test_graph/G1.txt','r')
    # G = original graph, T = graph after prim's algorithm
    G = nx.read_weighted_edgelist(graph_data, nodetype=int)
    T = prims_algorithm(G, 0, showCost, showGraph)
    
if int(val) == 2:#user input graph
    print("  Enter the edges. Enter -1 0 0 to finish data imput")
    print("  The syntax is Source Destination Weight.")
    print("I.E: 3(source vertex) 1(destination vertex) 3(weight of the edge)")
    src = dest = weight = 0
    i = 1
    G = nx.Graph()
    while True:
        src, dest, weight =  [int(x) for x in input(f'Input edge number {i}: ').split()]
        if src == -1: break;
        G.add_edge(src, dest, weight = weight)
        i+=1
        
    q = input("Show Cost (Y/N): ")
    showCost = True if not val=='Y' else False
    q = input("Show Graph (Y/N):")
    showGraph = True if not val=='Y' else False
    T = prims_algorithm(G, 0, showCost, showGraph)
print("Program Completed !")
