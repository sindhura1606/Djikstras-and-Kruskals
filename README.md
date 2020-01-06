# Djikstras-and-Kruskals
 
Dijkstra's algorithm: 
Dijkstra's algorithm (or Dijkstra's Shortest Path First algorithm, SPF algorithm), given a graph with vertices and edges connecting them, it finds the shortest distances of all the vertices from a given start vertex s. Graph should be a connected graph and edges can either be Directed/Undirected. Edge weights should be non-negative i.e. w(e)>=0
How it works:
•	The algorithm starts with the single source vertex, and grows the cloud or set of vertices, and covers all the vertices.
•	All the vertices adjacent to the source vertices are then added to a heap along with their edge distances and extract min from the queue
•	At each step, the vertex outside the cloud with minimum edge distance is then added to the cloud by relaxing the edges and update the labels of vertices adjacent to new added vertex in the cloud.
•	Repeat until all the connected vertices are added to the cloud, i.e is queue is empty
Time Complexity:
The run time implementation is  O(ElogV).
Kruskal’s Algorithm:
Kruskal's algorithm is a minimum-spanning-tree algorithm which finds an edge of the least possible weight that connects any two trees in the forest. Kruskal's algorithm uses greedy approach to find the minimum cost spanning tree. This algorithm treats the graph as a forest and every node it has as an individual tree. A tree connects to another only and only if, it has the least cost among all available options and does not violate MST properties. It sorts the edges of a graph in order of increasing cost and then repeatedly adds edges that bridge separate components. 
Steps to find MST using Kruskal’s:
•	For each vertex in graph, make a set V
•	Sort the edges G.E into non decreasing order of their weight
•	Pick the smallest edge and check for the cycle, discard if cycle is formed
•	Repeat above step for V-1 edges in the spanning tree
The runtime of this algorithm is O(ElogE) or O(ElogV). Sorting of the edges take O(ElogE) time. We then apply union find algorithm. Find and union takes at most O(logV). Value of E is less than V2. So, log E = O(log V). Therefore, overall time complexity is O(ElogE) or O(ElogV).

Data Structure Used:
•	We have used the disjoint-set (i.e. Union Find) data structure to implement Kruskal’s Algorithm.
•	We have used heap data structure to find single source shortest path using Dijkstra's algorithm
