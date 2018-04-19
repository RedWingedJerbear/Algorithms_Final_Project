import random
import sys
import time
import networkx as nx
import matplotlib.pyplot as plt


def minDistance(G, mst):
    min_key = sys.maxsize
    for edge in G.edges(mst):
        if edge[1] not in mst:
            if G[edge[0]][edge[1]]['weight'] < min_key:
                min_key = G[edge[0]][edge[1]]['weight']
                min_edge = [edge[0], edge[1], min_key]
    return min_edge


def prim(G, pos):
    mst = [0]
    v = G.subgraph(0).copy()
    for i in range(1, G.number_of_nodes()):
        edge = minDistance(G, mst)
        v.add_edge(edge[0], edge[1], weight=edge[2])
        mst.append(edge[1])
        G.add_edge(edge[0], edge[1], weight=edge[2], color='g')
        drawGraph(G, pos)
        plt.show()
        time.sleep(2)
    return pos


def drawGraph(G, pos):
    plt.ion()
    edges = G.edges()
    edge_colors = [G[u][v]['color'] for u,v in edges]
    nx.draw(G, pos, edges=edges, with_labels=True, node_color=edge_colors, edge_color=edge_colors)
    edge_labels = nx.get_edge_attributes(G, 'weight')
    nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels)
    return pos


n = int(input("Enter the number of nodes on the graph (> 4): "))

G = nx.random_regular_graph(4, n, seed=None)

for (u, v) in G.edges():
    G[u][v]['weight'] = random.randint(1, n)
    G[u][v]['color'] = 'r'

labels = []
nx.set_node_attributes(G, labels, 'labels')
labels.append('foo')
print(G[0]['labels'])
pos = nx.spring_layout(G)
drawGraph(G, pos)

prim(G, pos)

