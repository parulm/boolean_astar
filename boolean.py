#Library that contains functions for the AI 597 project
#The input network is in the sufficient necessary form. Nodes of the network contain an attribute called value which can be set to True or False.

#Update function takes the state space graph, the current state, the node to update, weight array or the particular weight or none and creates a new state i.e. vertex in the state space graph which represents the post update state; it also creates a directed arrow from the input state to the newly created state.
def update(T,G,current_id,vertex_id,found,wt=1):
	#Remove current_id from unvisited before proceeding
	#write the commented code here
	#Remember to consider the pseudo nodes appropriately
	#Delete the edge if it is creating a self loop
	return T

#Calculates estimated cost to get from the state to goal node; inputs a 2D array of node id's and corresponding Boolean values
def h(state,goal):
	#code here; h = sigma(wt_i*|goal_i - state_i|)
	return h_value

#The cost so far - incurred in reaching from initial state to state. The state must exist in the current version of the state space graph. T is the state transition graph. initial_id and state_id are the node id's in T of the initial and current states. To implement this, you will also need to have a 2D array where an integer key corresponds to a 2D array
def g(T,initial_id,state_id):
	#calculate the sum of edge weights along the shortest path
	return g_value

def create_state(T):
	n = T.number_of_nodes()
	T.add_node(n)
	#add to the unvisited list
	#set g value as infinity [infinity=1000 for this code] 
	#set h value
	return None

#A star search inputs the sufficient necessary form of the Boolean network; the goal state we are aiming to reach; & the initial state
#When to make it stop? - Make it stop when there are no outgoing edges from any of the leaf nodes (i.e., all the update operations are leading to self loops) - when should I check for this?
#Fix this for self loops
def astar(G, goal, initial):
	found = False
	#boolean_size = 1 #set this to be the number of non-pseudo nodes in the Boolean network
	#astar search
	#f = g + h
	T=nx.DiGraph
	T.add_node(0)
	#set 0 to correspond to the matrix initial
	minv=1000
	unvisited = [0]
	for node_id in T.nodes():
		#I have to look at only unvisited nodes
		if node_id not in unvisited:
			continue
		node_state = [[],[]] #set this variable to corresponding 2D matrix
		f = h(node_state,goal) + g(T,0,node_id)
		if f < minv:
			minv = f
			pref_id = node_id
	
	for b in G.nodes():
		wt_b = G[b]['weight']
		update(T,G,pref_id,b,wt_b,found)
		if found:
			return T, found
		else:
			continue