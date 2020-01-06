from collections import defaultdict 
import timeit

#Class to represent a graph 
class Graph: 

    def __init__(self,vertices):
        self.V = vertices 
        self.graph = []                     # default dictionary to store graph
    
    # function to add an edge in the graph 
    def Edge_Add(self,u,v,w): 
        self.graph.append([u,v,w]) 

    # This function finds the set of an element i using path compression technique
    def find(self, p, i): 
        if p[i] == i: 
            return i
        return self.find(p, p[i]) 

    # A function that does union of two sets of x and y using union by rank
    def union(self, parent, rank, x, y): 
        xroot = self.find(parent, x) 
        yroot = self.find(parent, y) 
        
        if rank[xroot] < rank[yroot]: 
            parent[xroot] = yroot 
        elif rank[xroot] > rank[yroot]: 
            parent[yroot] = xroot 
        else : 
            parent[yroot] = xroot 
            rank[xroot] += 1
            
    # The main function to construct MST using Kruskal's algorithm 
    def KruskalMST(self): 

        result =[] #This will store the result MST 

        i = 0 
        e = 0
        
        self.graph = sorted(self.graph,key=lambda item: item[2])

        prnt = [] ; rank = [] 

        for node in range(self.V+1): 
            prnt.append(node)
            rank.append(0) 

        
        while e < self.V-1 : 
            u,v,w = self.graph[i] 
            i = i + 1
            x = self.find(prnt, u) 
            y = self.find(prnt ,v) 
            
            if x != y:
                e = e + 1
                result.append([u,v,w]) 
                self.union(prnt, rank, x, y) 
        print( "Following are the edges in the constructed MST")
        print( "path   edge_cost")
        cost = 0
        for u,v,wght in result:
            cost=cost+wght
            print ("%d ----- %d = %d" % (u,v,wght)) 
        print("Cost of Minimum Spanning Tree is :",cost)    
        
start = timeit.default_timer()
#main
#reading the input from the file
with open('input1.txt') as file:                               #Text file name from whichinnput is to be read.
    file_lines = file.readlines()
    inp = [line.rstrip('\n').split(' ') for line in file_lines]

t = inp[0][2]
if t == 'D':
    print("It is a directed graph.Please input an undirected graph")
elif t == 'U':
    print("It is an undirected graph")

v=int(inp[0][0]) #No. of vertices 
g = Graph(v)
for i in range(1,len(inp)):
    g.Edge_Add(int(inp[i][0]),int(inp[i][1]),int(inp[i][2]))

g.KruskalMST()            #Call to Krushkal Algorithm
stop = timeit.default_timer()
print('Runtime: ', stop - start)
