from tkinter import font
import sys
from contextlib import contextmanager
from operator import ge
import gmplot
from geopy.geocoders import Nominatim
from matplotlib.pyplot import plot
from collections import defaultdict
from ctypes import sizeof
from importlib.resources import path
from turtle import distance
from numpy import append, size
 
class Graph:
    def __init__(self) -> None:
        self.path=[]
    # A utility function to find the
    # vertex with minimum dist value, from
    # the set of vertices still in queue
    def minDistance(self,dist,queue):
        # Initialize min value and min_index as -1
        minimum = float("Inf")
        min_index = -1
         
        # from the dist array,pick one which
        # has min value and is till in queue
        for i in range(len(dist)):
            if dist[i] < minimum and i in queue:
                minimum = dist[i]
                min_index = i
        return min_index
 
 
    # Function to print shortest path
    # from source to j
    # using parent array
    # Mode 0 defines the append mode
    # It will only append the intermediate node of minimum distance path
    def printPath(self, parent, j,mode=1):
        #Base Case : If j is source
        # path = []
        if parent[j] == -1:
            if mode==0:
                self.path.append(j)
            else:
                print(j,end=" ")
            return
        self.printPath(parent , parent[j],mode)
        if mode==0:
            self.path.append(j)
        else:
            print (j,end=" ")

 
    # A utility function to print
    # the constructed distance
    # array
    def printSolution(self,src, dist, parent):
    
        print("Vertex \t\tDistance from Source\tPath")
        for i in range(1, len(dist)):
            if (i == 1 or i==13 or i == 3):
                print ("\n%d --> %d \t\t%.2f \t\t\t\t\t" % (src, i, dist[i]),end=" ")
                self.printPath(parent,i)
        minimum = 100
        min = 0
        for i in range (1, len(dist)):
            if (i == 1 or i==13 or i == 3):
                # if (dist [i] < minimum and dist [i] != 0):
                if (dist [i] < minimum ):
                    minimum = dist [i]
                    min=i
        
        print ("\nMinimum distance", minimum)
        for i in range(1, len(dist)):
                if minimum == dist[i]:
                    break
        return (min,minimum)
        #return(self.printPath(parent, i))
 
    '''Function that implements Dijkstra's single source shortest path
    algorithm for a graph represented using adjacency matrix
    representation'''
    def dijkstra(self, graph, src):
 
        row = len(graph)
        col = len(graph[0])
 
        # The output array. dist[i] will hold
        # the shortest distance from src to i
        # Initialize all distances as INFINITE
        dist = [float("Inf")] * row
 
        #Parent array to store
        # shortest path tree
        parent = [-1] * row
 
        # Distance of source vertex
        # from itself is always 0
        dist[src] = 0
     
        # Add all vertices in queue
        queue = []
        for i in range(row):
            queue.append(i)
             
        #Find shortest path for all vertices
        while queue:
 
            # Pick the minimum dist vertex
            # from the set of vertices
            # still in queue
            u = self.minDistance(dist,queue)
 
            # remove min element    
            queue.remove(u)
 
            # Update dist value and parent
            # index of the adjacent vertices of
            # the picked vertex. Consider only
            # those vertices which are still in
            # queue
            for i in range(col):
                '''Update dist[i] only if it is in queue, there is
                an edge from u to i, and total weight of path from
                src to i through u is smaller than current value of
                dist[i]'''
                if graph[u][i] and i in queue:
                    if dist[u] + graph[u][i] < dist[i]:
                        dist[i] = dist[u] + graph[u][i]
                        parent[i] = u
 
 
        # print the constructed distance array
        dest,dist_min = self.printSolution(src,dist,parent)
        # self.path.append(src)
        self.printPath(parent,dest,mode=0)
        #print(self.path)
 
g= Graph()
 
graph = [[0, 4.4, 0, 0, 0, 0, 3.5, 0, 0, 0, 0, 0, 0, 0],
        [4.4, 0, 10, 0, 7, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 10, 0, 5, 0, 0, 14, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 5, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 7, 0, 0, 0, 6, 0, 0, 0, 0, 0, 0, 0 ,0],
        [0, 0, 0, 0, 6, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [3.5, 0, 14, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 1, 0, 6, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 6, 0, 3, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 3, 0, 2, 0, 3, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 2, 0, 2, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 2, 0, 4, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 3, 0, 4, 0, 5],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 5, 0]]

# Print the solution
#g.dijkstra(graph,g.source)
#g.path.append(15)
#print(g.path)
def mapping(start):
    geolocator = Nominatim(user_agent="MyApp")
    g.dijkstra(graph, start)
    print (g.path)
    # print(location_index)
    lat1 = [12.975484,12.948589, 12.960445, 12.930120, 12.948951, 12.900965, 13.011400,13.007901, 13.052235, 
    13.070740, 13.085394, 13.084681, 13.074903, 13.079881]
    long1 = [80.220747,80.209967, 80.145306,80.121159, 80.240686, 80.227897,  80.223165, 80.203698, 80.211965, 
    80.203902, 80.198503, 80.217915, 80.217945, 80.261328]
    locdic=["Velachery", "Kamatchi Hospital-", "Chrompet", "Tambaram", "Thoraipakkam","Shollinganallur", "Guindy", "Kathipara", 
    "Vadapalani", "CMBT", "Thirumangalam", "Anna Nagar", "Aminjikarai", "Egmore"]
    b = g.path 
    plotlat = [None] * len(b)
    plotlong = [None] * len (b)
    intloc = [None] * len(b)
    for i in range (0, len (b)):
        plotlat [i] = lat1 [b[i]]
        plotlong [i] = long1 [b[i]]
        intloc [i] = locdic[b[i]]
#lat2 = [12.949108, 12.948484, 12.975550, 12.981455, 12.979972]
#long2 = [80.240708, 80.209945, 80.220818, 80.231899, 80.252635]
    print  (plotlat)
    print (plotlong)
    print (intloc)
    #return intloc
    gmapOne = gmplot.GoogleMapPlotter(13.010072, 80.222505, 12)
    gmapOne.marker (12.948589, 80.209967, name = "BLOOD BANK")
    gmapOne.marker (12.930120, 80.121159, name = "BLOOD BANK")
    gmapOne.marker (13.079881, 80.261328, name = "BLOOD BANK")
    gmapOne.scatter (plotlat, plotlong, '#00FFFF', size = 50, marker = True)
    gmapOne.plot (plotlat, plotlong, 'blue', edge_width = 2.5)
#gmapOne.scatter (lat2, long2, '#00FFFF', size = 50, marker = False)
#gmapOne.plot (lat2, long2, 'yellow', edge_width = 2.5)
    gmapOne.draw("E:\\ADS PROJECT PYTHON\\Program files\\mappy.html")
