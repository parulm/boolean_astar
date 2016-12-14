#execute A star search on the state transition graph of a given Boolean network

import time
import timeit
import boolean1
import importlib
import gprops
import networkx as nx
from time import sleep


#read the graph in sufficient necessary format using the importlib
filename = 'file.txt'
G = importlib.read_boolean(filename)

gprops.set_edge_type(G)

#Set initial values
for node in G.nodes():
	G.node[node]['value'] = False

#Set weights. Ideally, you should type down everything manually
c=1
for node in G.nodes():
	G.node[node]['weight'] = 0.01*(c**2) - 0.25*c + 2
	c+=1

print G.nodes()

print 'Now that you know the node sequence, please enter the initial and goal states'
initial = input('Enter the initial state: ')
goal = input('Enter the goal state: ')
#start = time.clock()
start2 = timeit.default_timer()
#goal = '111'
#initial = '010'

#T = nx.DiGraph()

T = boolean1.astar(G, goal, initial)

outf = '/home/parul/Dropbox/psu/597 AI/project/graphs/astar_3.graphml'
#nx.write_graphml(T,outf)

#stop = time.clock()
#print stop-start
stop2 = timeit.default_timer()
print (stop2-start2)
