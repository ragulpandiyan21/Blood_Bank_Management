from tkinter import font
import sys
from contextlib import contextmanager
from operator import ge
import gmplot
from geopy.geocoders import Nominatim
from SearchBB import *
geolocator = Nominatim(user_agent="MyApp")
#a = Graph()
# c= S.source
#a.dijkstra(graph,c)
#print (a.path)

lat1 = [12.975484,12.948589, 12.960445, 12.930120, 12.948951, 12.900965, 13.011400,13.007901, 13.052235, 13.070740, 13.085394, 13.084681, 13.074903, 13.079881]
long1 = [80.220747,80.209967, 80.145306,80.121159, 80.240686, 80.227897,  80.223165, 80.203698, 80.211965, 80.203902, 80.198503, 80.217915, 80.217945, 80.261328]
#b = a.path 
#plotlat = [None] * len(b)
#plotlong = [None] * len (b)

#for i in range (0, len (b)):
#    plotlat [i] = lat1 [b[i]]
#    plotlong [i] = long1 [b[i]]
#lat2 = [12.949108, 12.948484, 12.975550, 12.981455, 12.979972]
#long2 = [80.240708, 80.209945, 80.220818, 80.231899, 80.252635]

gmapOne = gmplot.GoogleMapPlotter(13.010072, 80.222505, 12)
gmapOne.marker (12.975484, 80.220747, name = "Velachery")
gmapOne.scatter (plotlat, plotlong, '#00FFFF', size = 50, marker = False)
gmapOne.plot (plotlat, plotlong, 'blue', edge_width = 2.5)
#gmapOne.scatter (lat2, long2, '#00FFFF', size = 50, marker = False)
#gmapOne.plot (lat2, long2, 'yellow', edge_width = 2.5)
gmapOne.draw("E:\\ADS PROJECT PYTHON\\mappy.html")