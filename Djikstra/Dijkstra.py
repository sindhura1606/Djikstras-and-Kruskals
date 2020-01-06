import sys
import heapq
import timeit
class Vertex:
    def __init__(self, node):
        self.id = node
        self.adjacent = {}
        # Set distance to infinity for all nodes
        self.distance = sys.maxsize        # Mark all nodes unvisited        
        self.visited = False  
        # Predecessor
        self.previous = None

    def add_neighbor(self, neighbor, weight=0):
        self.adjacent[neighbor] = weight

    def get_connections(self):
        return self.adjacent.keys()  

    def get_id(self):
        return self.id

    def get_weight(self, neighbor):
        return self.adjacent[neighbor]

    def set_distance(self, dist):
        self.distance = dist

    def get_distance(self):
        return self.distance

    def set_previous(self, prev):
        self.previous = prev

    def set_visited(self):
        self.visited = True

    def __str__(self):
        return str(self.id) + ' adjacent: ' + str([x.id for x in self.adjacent])
    
    def __lt__(self,other):
        return self.get_distance()<other.get_distance()

class Graph:
    def __init__(self):
        self.vert_dict = {}
        self.num_vertices = 0

    def __iter__(self):
        return iter(self.vert_dict.values())

    def add_vertex(self, node):
        self.num_vertices = self.num_vertices + 1
        new_vertex = Vertex(node)
        self.vert_dict[node] = new_vertex
        return new_vertex

    def get_vertex(self, n):
        if n in self.vert_dict:
            return self.vert_dict[n]
        else:
            return None

    def add_edge(self, frm, to, cost = 0):
        if frm not in self.vert_dict:
            self.add_vertex(frm)
        if to not in self.vert_dict:
            self.add_vertex(to)

        self.vert_dict[frm].add_neighbor(self.vert_dict[to], cost)
        self.vert_dict[to].add_neighbor(self.vert_dict[frm], cost)

    def get_vertices(self):
        return self.vert_dict.keys()

    def set_previous(self, current):
        self.previous = current

    def get_previous(self, current):
        return self.previous

def shortest(v, path):
    ''' make shortest path from v.previous'''
    if v.previous:
        path.append(v.previous.get_id())
        shortest(v.previous, path)
    return



def dijkstra(aGraph, start, target):
    #print '''Dijkstra's shortest path'''
    # Set the distance for the start node to zero 
    start.set_distance(0)

    # Put tuple pair into the priority queue
    unvisited_queue = [(v.get_distance(),v) for v in aGraph]
    heapq.heapify(unvisited_queue)
    
    while len(unvisited_queue):
        # Pops a vertex with the smallest distance 
        uv = heapq.heappop(unvisited_queue)
        current = uv[1]
        current.set_visited()

        #for next in v.adjacent:
        for next in current.adjacent:
            # if visited, skip
            if next.visited:
                continue
            new_dist = current.get_distance() + current.get_weight(next)
           # print(dtype(new_dist))
            if (new_dist) < (next.get_distance()):
                next.set_distance(new_dist)
                next.set_previous(current)
                print ('updated : current = %s next = %s new_dist = %s' %(current.get_id(), next.get_id(), next.get_distance()))
            else:
                print ('not updated : current = %s next = %s new_dist = %s'  %(current.get_id(), next.get_id(), next.get_distance()))

        # Rebuild heap
        # 1. Pop every item
        while len(unvisited_queue):
            heapq.heappop(unvisited_queue)
        # 2. Put all vertices not visited into the queue
        unvisited_queue = [(v.get_distance(),v) for v in aGraph if not v.visited]
        heapq.heapify(unvisited_queue)
    
if __name__ == '__main__':
    #Enter input file name 
    start_time = timeit.default_timer()
    with open('graph1.txt') as file:
        file_lines = file.readlines()
        y = [line.rstrip('\n').split(' ') for line in file_lines]
    print(y)
    
    #edge_list=[]
    tree_nodes=set()
    for i in range(1,len(y)):
        if(i==len(y)-1):
            src=str(y[i][0])
            dest=str(y[i][1])
            print("source",src)
            break
        else:
            tree_nodes.add(str(y[i][0]))
            tree_nodes.add(str(y[i][1]))
    g = Graph()
    for i in range(len(tree_nodes)):
        g.add_vertex(i)
    
    for j in range(1,len(y)-1):
        g.add_edge(str(y[j][0]),str(y[j][1]),int(y[j][2]))
     
    t=y[0][2]
    if t == 'D':
        print("It is a directed graph.Please input an undirected graph")
    elif t == 'U':
        print("It is an undirected graph")

    dijkstra(g, g.get_vertex(src), g.get_vertex(dest)) 

    target = g.get_vertex(dest)
    path = [target.get_id()]
    shortest(target, path)
    cost = target.get_distance()
    print ('The shortest path : %s' %(path[::-1]),"Cost is:",cost)
    stop_time = timeit.default_timer()
    print('Runtime: ', stop_time - start_time)