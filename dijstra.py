import math
from heapq import heappush, heappop

INF = 0xffffffffff
dist = {}
prev = {}


class Node:

    def __init__(self, point):
        self.point = point

    def __lt__(self, other):
        return dist[self.point] < dist[self.point]


class Graph:

    def __init__(self):
        self.graph = {}

    def add_edge(self, u, v):
        if u in self.graph.keys():
            self.graph[u].append(v)
        else:
            self.graph[u] = [v]
            dist[u] = 0xffffffffff
            
        if v in self.graph.keys():
            self.graph[v].append(u)
        else:
            self.graph[v] = [u]
            dist[v] = INF

 
def distance(point1, point2):
    x = point1[0] - point2[0]
    y = point1[1] - point2[1]
    return math.sqrt(x * x + y * y)


graph = Graph()

graph.add_edge((1, 1), (2, 2))
graph.add_edge((2, 2), (3, 3))
graph.add_edge((3, 3), (5, 5))
graph.add_edge((2, 2), (5, 5))


def dijstra(source, destination):
    prev[source] = None
    heap = []
    heappush(heap, source)
    dist[source] = 0
    while heap:
        node = heappop(heap)
        if node == destination:
            return 
        for i in graph.graph[node]:
            cost = distance(node, i)
            if dist[node] + cost < dist[i] :
                dist[i] = dist[node] + cost
                heappush(heap, i)
                prev[i] = node
    return 

  
def print_path(dest):

    if(dest == None):
        return 
    print_path(prev[dest])
    print(dest)

      
dijstra((1, 1), (5, 5))
print_path((5, 5))