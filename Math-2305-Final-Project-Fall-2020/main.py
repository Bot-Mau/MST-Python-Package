import networkx as nx
from algorithms import prims_algorithm

#the function asks whether the user wishes to see an example graph from text file graph
#or to input their own graph
val = input("Indicate (1) if you want to see example graph or (2) to input the graph: ")
if int(val) == 1:
    #show an example graph from G1.txt file to the user.
    #the user input Y or N in order to see cost (of the graph) and the graph
    q = input("Show Cost (Y/N): ")
    showCost = True if not val=='Y' else False
    q = input("Show Graph (Y/N):")
    showGraph = True if not val=='Y' else False
    #read graph from file
    graph_data = open('test_graph/G1.txt','r')
    # G = original graph, T = graph after prim's algorithm
    G = nx.read_weighted_edgelist(graph_data, nodetype=int)
    T = prims_algorithm(G, 0, showCost, showGraph)
    
if int(val) == 2:
    #user input graph requests user to input their desired graph using syntax: x x x.
    #after that the program asks user Y and N in order to show the cost of their graph
    #and the graph
    print("  Enter the edges. Enter -1 0 0 to finish data imput")
    print("  The syntax is Source Destination Weight.")
    print("I.E: 3(source vertex) 1(destination vertex) 3(weight of the edge)")
    src = dest = weight = 0
    i = 1
    G = nx.Graph() #create an empty graph
    while True:
        #src = source node, dest = destination node, weight = value of the edge
        #the program read the input of the user, if the input starts with -1. the loop exterminates
        src, dest, weight =  [int(x) for x in input(f'Input edge number {i}: ').split()]
        if src == -1: break;   #check point whether the input is processed 
        G.add_edge(src, dest, weight = weight) #add an edge to the graph G
        i+=1
        
    q = input("Show Cost (Y/N): ")
    showCost = True if not val=='Y' else False
    q = input("Show Graph (Y/N):")
    showGraph = True if not val=='Y' else False
    T = prims_algorithm(G, 0, showCost, showGraph)
print("Program Completed !")
