#Library that contains functions for the AI 597 project
#The input network is in the sufficient necessary form. Nodes of the network contain an attribute called value which can be set to True or False.
#Modified from boolean.py in the sense that it assumes straightforward Boolean functions, i.e., the suff-necc network has no pseudo nodes.

import gprops
import networkx as nx

#Update function takes the state space graph, the current state, the node to update, weight array or the particular weight or none and creates a new state i.e. vertex in the state space graph which represents the post update state; it also creates a directed arrow from the current state to the newly created state.
def update(T,G,current,nid,unvisited,nlist,wt):
	#print 'current is:', current,'and unvisited is:', unvisited
	if current in unvisited:
		pass
		#unvisited.remove(current)
	else:
		#print 'Error: The state',current,'is either not created or already visited'
		return None
	clist = list(current)
	new_list = clist
	up_node = nlist[nid]
	parents = G.predecessors(up_node)
	if len(parents)==0:
		return T
	elif len(parents)==1:
		p_node = parents[0]
		p = nlist.index(p_node)
		new_list[nid] = clist[p]
	else:
		plist = []
		for par in parents:
			pid = nlist.index(par)
			plist.append(clist[pid])
		ntype = gprops.node_type(G, up_node)
		if ntype=='red':
			new_val = 0
			for i in range(len(plist)):
				ival = int(plist[i])
				par_node = parents[i]
				#print 'Verification: Parent',par_node,'has value',ival
				if G[par_node][up_node]['arrowhead'] == 'tee':
					new_val = int(bool(new_val) or not bool(ival))
				else:
					new_val = int(bool(new_val) or bool(ival))
		elif ntype=='blue':
			new_val = 1
			for j in range(len(plist)):
				ival = int(plist[j])
				par_node = parents[j]
				#print 'Verification: Parent',par_node,'has value',ival
				if G[par_node][up_node]['arrowhead'] == 'tee':
					new_val = int(bool(new_val) and not bool(ival))
				else:
					new_val = int(bool(new_val) and bool(ival))
		else:
			print 'Ran into an error. Node type was not defined.'
	new_list[nid] = str(new_val)
	#print new_list
	new_state = "".join(new_list)
	if new_state!=current:
		T.add_node(new_state)
		T.node[new_state]['label'] = new_state
		unvisited.append(new_state)
		T.add_edge(current,new_state,weight=wt)
	#Remember to consider the pseudo nodes appropriately
	return T

#Calculates estimated cost to get from the state to goal node; inputs a 2D array of node id's and corresponding Boolean values
def h(state,goal,wt):
	slist = list(state)
	glist = list(goal)
	#print 'slist:',slist
	#print 'glist:',glist
	h_value = 0
	for i in range(len(slist)):
		if slist[i]==glist[i]:
			pass
		else:
			h_value+=wt[i]
	return h_value

#The cost so far - incurred in reaching from initial state to state. The state must exist in the current version of the state space graph. T is the state transition graph. initial_id and state_id are the node id's in T of the initial and current states. To implement this, you will also need to have a 2D array where an integer key corresponds to a 2D array
def g(T,initial,state):
	g_value = nx.dijkstra_path_length(T,initial,state)
	return g_value

'''
def create_state(T):
	n = T.number_of_nodes()
	T.add_node(n)
	#add to the unvisited list
	#set g value as infinity [infinity=1000 for this code] 
	#set h value
	return None
'''

def best_first(T,unvisited,wt,goal,initial):
	minv = 1000
	for node in T.nodes():
		#I have to look at only unvisited nodes
		if node not in unvisited:
			continue
		#node_state = [[],[]] #set this variable to corresponding 2D matrix
		f = h(node,goal,wt) + g(T,initial,node)
		#print 'For node', node, 'evaluation function is',f
		if f < minv:
			minv = f
			pref = node
	#print 'We chose node',pref,'\n'
	return pref

#A star search inputs the sufficient necessary form of the Boolean network; the goal state we are aiming to reach; & the initial state
#When to make it stop? - Make it stop when there are no outgoing edges from any of the leaf nodes (i.e., all the update operations are leading to self loops) - when should I check for this?
#Fix this for self loops
def astar(G, goal, initial):
	#T = nx.DiGraph()
	nlist = G.nodes()
	wt=[]
	for i in range(len(nlist)):
		Gnode = nlist[i]
		wt.append(G.node[Gnode]['weight'])
	found = False
	#boolean_size = 1 #set this to be the number of non-pseudo nodes in the Boolean network
	#astar search
	#f = g + h
	print wt
	T=nx.DiGraph()
	T.add_node(initial)
	T.node[initial]['label'] = initial
	unvisited = [initial]
	while unvisited:
		#print unvisited
		#print nlist
		current = best_first(T, unvisited, wt, goal, initial)
		#print current
		#unvisited.remove(current)
		for i in range(len(nlist)):
			#print 'at',i,'th iteration. Current is:', current,'will update node:',nlist[i]
			wt_i = wt[i]
			update(T, G, current, i, unvisited, nlist, wt_i)
			if goal in unvisited:
				print 'Found the goal!'
				found = True
				return T
		unvisited.remove(current)
	if not found:
		print 'Could not find the goal'
	return T