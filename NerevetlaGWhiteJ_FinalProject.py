import random
import networkx as nx
from networkx_viewer import Viewer

#def prims():

n = int(input("Enter the number of nodes on the graph (> 4): "))

G = nx.random_regular_graph(4, n, seed=None)

for (u, v) in G.edges():
    G.edge[u][v]['weight'] = random.randint(1, n)


app = Viewer(G)
app.mainloop()
