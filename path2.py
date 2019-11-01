import math
from heapq import heappush, heappop
import csv
import simplekml
from math import sin, cos, sqrt, atan2, radians
import sys
import numpy as np

sys.setrecursionlimit(500000000)


INF = 0xffffffffff
dist = {}
prev = {}
list_of_point = []


class Node:

    def __init__(self, point):
        self.point = point

    def __lt__(self, other):
        return dist[self.point] < dist[other.point]


class Graph:

    def __init__(self):
        self.graph = {}

    def add_edge(self, u, v):
        if u in self.graph.keys():
            self.graph[u].append(v)
        else:
            self.graph[u] = [v]
        dist[u] = INF
            
        if v in self.graph.keys():
            self.graph[v].append(u)
        else:
            self.graph[v] = [u]
        dist[v] = INF

def distance(point1, point2):
    R = 6373.00
    lat1 = radians(point1[1])
    lon1 = radians(point1[0])
    lat2 = radians(point2[1])
    lon2 = radians(point2[0])
    dlon = lon2 - lon1
    dlat = lat2 - lat1
    a = sin(dlat / 2)**2 + cos(lat1) * cos(lat2) * sin(dlon / 2)**2
    c = 2 * atan2(sqrt(a), sqrt(1 - a))
    return (R * c)


class Adja:

    def __init__(self):
        self.adj = dict()

    def add_edge(self, u, v, mode):
        self.adj[v] = {u: mode}
        self.adj[u] = {v: mode}


adj = Adja()
graph = Graph()

with open('Routemap-DhakaMetroRail.csv') as csvfile:
    readCSV = csv.reader(csvfile, delimiter=',')
    for row in readCSV:
        lst = []
        i = 1
        while i < len(row)-3:
          lst.append((float(row[i]), float(row[i+1])))
          i = i+2
        i = 0
        for p in lst:
            list_of_point.append(p)
        while i < len(lst)-1:
            adj.add_edge(lst[i], lst[i+1], 'metro')
            graph.add_edge(lst[i], lst[i+1])
            i = i+1


with open('Roadmap-Dhaka.csv') as csvfile:
    readCSV = csv.reader(csvfile, delimiter=',')
    for row in readCSV:
        lst = []
        i = 1
        while i < len(row)-3:
          lst.append((float(row[i]), float(row[i+1])))
          i = i+2
        i = 0
        for p in lst:
            list_of_point.append(p)
        while i < len(lst)-1:
            graph.add_edge(lst[i], lst[i+1])
            i = i+1
  
def dijkstra(source, destination):
    prev[source] = None
    heap = []
    node = Node(source)
    heappush(heap, node)
    dist[source] = 0
    k = 0
    while heap:
        node = heappop(heap)
        for i in graph.graph[node.point]:
            k = k+1
            cost = distance(node.point, i)
            try:
                if adj.adj[node.point][i] == 'metro':
                    cost = cost*5
            except KeyError:
                cost = cost*20
                #print('caaaaaaaaaaaaaaaaaaaaar')

            if dist[node.point] + cost < dist[i] :
                dist[i] = dist[node.point] + cost
                heappush(heap, Node(i))
                prev[i] = node.point
    return k

res = []

  
def print_path(dest):

    if(dest == None):
        return 
    print_path(prev[dest])
    res.append(dest)

s = (90.390537, 23.823028)
d = (90.440527, 23.745232)


def closest_node(node, nodes):
    pt = []
    dist = 9999999
    for n in nodes:
        if distance(node, n) <= dist:
            dist = distance(node, n)
            pt = n
    return pt

ss = closest_node(s, list_of_point)
dd = closest_node(d, list_of_point)

print(dijkstra(ss,dd))
print_path(dd)

i = 0
pr = 1
check = True
while i < len(res)-1:
    try:
        if(adj.adj[res[i]][res[i+1]] == 'metro'):
            if check:
                check = False
                print('Ride a metrorail from point ', end='')
                print(res[i], end=' to ')
                pr = 1
            if pr == 0:
                print(res[i+1])
            if pr == 1:
                i = i + 1
                continue
            pr = 1
            print('Ride a metrorail from point ', end='')
            print(res[i], end=' to ')
    except KeyError:
        if check:
            check = False
            print('Ride a car from point ', end='')
            print(res[i], end=' to ')
            pr = 0
        if pr == 1:
                print(res[i+1])
        if pr == 0:
            i = i + 1
            continue
        pr = 0
        print('Ride a car from point ', end='')
        print(res[i], end=' to ')
    i = i + 1
print(res[len(res)-1])
kml = simplekml.Kml()
kml.newlinestring(coords=res)
kml.save('road2.kml')
