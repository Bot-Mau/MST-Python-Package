import networkx as netx
import matplotlib.pyplot as plt

def show_weighted_graph(G):
    #the function draws a graph, and label edge with weight
    pos = netx.planar_layout(G)
    netx.draw(G, pos)
    labels = netx.get_edge_attributes(G, 'weight')
    netx.draw_networkx_edge_labels(G, pos, edge_labels= labels)
    plt.show()
    
def draw_subtree(G, T):
    #the function draw a sub_graph T from main tree G
    pos = netx.planar_layout(G)
    netx.draw_networkx(G, pos)
    labels = netx.get_edge_attributes(G, 'weight')
    netx.draw_networkx(G, pos, with_labels=True)
    netx.draw_networkx_edge_labels(G, pos, edge_labels= labels)
    netx.draw_networkx_edges(G, pos, edgelist=T.edges(), width=5, alpha=0.5, edge_color='g',)
    netx.draw_networkx_nodes(G, pos, nodelist=T.nodes(), node_color='b', node_size=500, alpha=0.5)
    plt.show()
