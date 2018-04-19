import random
import sys
import time
import networkx as nx
import matplotlib.pyplot as plt
from networkx_viewer import Viewer


def minDistance(G, mst, v):
    min_key = sys.maxsize
    for edge in G.edges(mst):
        if edge not in v:
            if G.edge[edge[0]][edge[1]]['weight'] < min_key:
                min_key = G.edge[edge[0]][edge[1]]['weight']
                min_edge = [edge[0], edge[1], min_key]
    return min_edge


def prim(G, pos):
    mst = [0]
    v = G.subgraph(0)
    for i in range(1, G.number_of_nodes() - 1):
        edge = minDistance(G, mst, v)
        v.add_edge(edge[0], edge[1], weight=edge[2])
        mst.append(edge[1])
        G.node[edge[1]]['color'] = 'g'
        G.edge[edge[0]][edge[1]]['color'] = 'g'
        updateGraph(G, pos)
        time.sleep(2)
    return pos


def drawGraph(G):
    plt.ion()
    pos = nx.spring_layout(G)
    edges = G.edges()
    colors = [G[u][v]['color'] for u,v in edges]
    nx.draw(G, pos, edges=edges, with_labels=True, edge_color=colors)
    edge_labels = nx.get_edge_attributes(G, 'weight')
    nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels)
    return pos

def updateGraph(G, pos):
    nodes = G.nodes()
    #node_colors = [i['color'] for i in G.nodes]
    #edge_colors = nx.get_edge_attributes(G, 'weight')
    nx.draw_networkx_nodes(G, pos, nodelist=nodes)
    nx.draw_networkx_edges(G, pos, edgelist=G.edges())
    plt.plot()
    return

n = int(input("Enter the number of nodes on the graph (> 4): "))

G = nx.random_regular_graph(4, n, seed=None)


for (u, v) in G.edges():
    G.edge[u][v]['weight'] = random.randint(1, n)
    G.edge[u][v]['color'] = 'r'

nx.set_node_attributes(G, 'color', 'r')
pos = drawGraph(G)
plt.plot()

prim(G, pos)

plt.show()
