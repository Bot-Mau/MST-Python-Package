import networkx as netx
import matplotlib.pyplot as plt

def show_weighted_graph(G):
    pos = netx.planar_layout(G)
    netx.draw(G, pos)
    labels = netx.get_edge_attributes(G, 'weight')
    netx.draw_networkx_edge_labels(G, pos, edge_labels= labels)
    plt.show()
    
def draw_subtree(G, T):
    pos = netx.planar_layout(G)
    netx.draw_networkx(G, pos)
    labels = netx.get_edge_attributes(G, 'weight')
    netx.draw_networkx(G, pos, with_labels=True)
    netx.draw_networkx_edge_labels(G, pos, edge_labels= labels)
    netx.draw_networkx_edges(G, pos, edgelist=T.edges(), width=0, alpha=0.5, edge_color='r',)
    netx.draw_networkx_nodes(G, pos, nodelist=T.nodes(), node_color='r', node_size=500, alpha=0.8)
    plt.show()
