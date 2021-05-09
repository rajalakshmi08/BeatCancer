# -*- coding: utf-8 -*-
"""
Created on Thu Nov 26 23:11:42 2020

@author: Raji
"""


import json
import scipy.spatial.distance as sc
import operator
from itertools import repeat
from operator import itemgetter
import math
import csv
import pandas as pd
import numpy as np

df_Locations = data = pd.read_csv('D:\\Raji\\2ndSemester\\S&O\\Assessment\\sample\\SaO_Optilandia_locations.csv')
df_Locations['capacity'] = df_Locations['capacity'].fillna(0)
df_Locations['level'] = df_Locations['level'].fillna(0)
df_Locations['difference'] = df_Locations['capacity'] - df_Locations['level']

def manhattanDistance( xy1, xy2 ):
    "Returns the Manhattan distance between points xy1 and xy2"
    return abs( xy1[0] - xy2[0] ) + abs( xy1[1] - xy2[1] )

def euclideanDistance( xy1, xy2 ):
    "Returns the Euclidean distance between points xy1 and xy2"
    return  math.sqrt(( xy2[0] - xy1[0] )**2 + ( xy2[1] - xy1[1] )**2)


def calculateRouteCost(r,capacityafterserving):
    total = 0
    for i in range(len(r) - 1):
        total+= euclideanDistance(r[i] , r[i+1]) * (2 + (capacityafterserving[i]* 0.5) )
        #vehicleCap = vehicleCap - 
    return total
    return total

def addDepotAtEnds(depot,route):
    route.insert(0,depot)
    route.append(depot)

#compute Savings for depot and i,j where i <> j
def computeSaving(depot, i,j):
    iDepot = manhattanDistance(i, depot)
    jDepot = manhattanDistance(depot, j)
    ijDist = manhattanDistance(i, j)
    
    return (iDepot + jDepot - ijDist)


def allCustomersConsidered(customerServed):
    for val in customerServed.values():
        if val == False:
            return False
    return True

def capacityValid(existing,new):
    totalCap = customerPositionDemand[new]
    for c in existing:
        totalCap+=customerPositionDemand[c]

    return totalCap <= vehicleCap

def isServed(c):
    return customerServed[c]

def hasBeenServed(c):
    customerServed[c] = True             


depot523Customers = [523, 8, 27, 70, 82, 94, 136, 183, 225, 235, 255, 257, 276, 378, 391, 491, 519, 585, 603, 632]

custlist523 = []

for i in range(0,len(depot523Customers)):
    list2 = [df_Locations.iloc[depot523Customers[i]]['id'], df_Locations.iloc[depot523Customers[i]]['x'],df_Locations.iloc[depot523Customers[i]]['y'],df_Locations.iloc[depot523Customers[i]]['difference']]
    custlist523.append(list2)

print (custlist523)


vehicleCapacity = [5,5,12,12,22]
#custlist = [[49581.9444, 6226.6667, 0.0], [49616.6667, 6233.3333, 0.19999999999999996], [49538.0556, 6284.1667, 1.02], [49561.9444, 6221.6667, 1.46], [49562.7778, 6364.4444, 0.6], [49511.6667, 6356.9444, 1.52], [49542.2222, 6150.0, 0.33999999999999997], [49616.6667, 6266.6667, 0.3999999999999999], [49619.4444, 6240.0, 0.64], [49585.2778, 6255.5556, 0.36], [49650.8333, 6303.6111, 0.16999999999999998], [49572.7778, 6248.6111, 0.19999999999999996], [49516.6667, 6166.6667, 0.9299999999999999], [49632.5, 6220.8333, 0.54], [49506.6667, 6150.5556, 1.0], [49520.0, 6298.3333, 0.33999999999999997], [49540.8333, 6259.7222, 0.21000000000000002], [49626.3889, 6336.9444, 1.41], [49540.2778, 6129.1667, 0.86], [49530.8333, 6355.0, 1.24]]
custlist523 = [[523, 49581.9444, 6226.6667, 0.0], [8, 49616.6667, 6233.3333, 0.19999999999999996], [27, 49538.0556, 6284.1667, 1.02], [70, 49561.9444, 6221.6667, 1.46], [82, 49562.7778, 6364.4444, 0.6], [94, 49511.6667, 6356.9444, 1.52], [136, 49542.2222, 6150.0, 0.33999999999999997], [183, 49616.6667, 6266.6667, 0.3999999999999999], [225, 49619.4444, 6240.0, 0.64], [235, 49585.2778, 6255.5556, 0.36], [255, 49650.8333, 6303.6111, 0.16999999999999998], [257, 49572.7778, 6248.6111, 0.19999999999999996], [276, 49516.6667, 6166.6667, 0.9299999999999999], [378, 49632.5, 6220.8333, 0.54], [391, 49506.6667, 6150.5556, 1.0], [491, 49520.0, 6298.3333, 0.33999999999999997], [519, 49540.8333, 6259.7222, 0.21000000000000002], [585, 49626.3889, 6336.9444, 1.41], [603, 49540.2778, 6129.1667, 0.86], [632, 49530.8333, 6355.0, 1.24]]
#custlist116 = [[116, 49804.1667, 6253.8889, 0.0], [5, 49757.7778, 6353.3333, 0.09999999999999998], [31, 49866.6667, 6216.6667, 0.56], [32, 49963.6111, 6124.1667, 0.92], [41, 49710.0, 6500.2778, 1.03], [64, 49894.4444, 6163.6111, 0.96], [65, 49700.0, 6433.3333, 0.72], [73, 49967.2222, 6167.7778, 0.22999999999999998], [77, 49811.3889, 6478.3333, 1.47], [80, 49830.0, 6171.9444, 0.22999999999999998], [110, 49830.5556, 6098.6111, 1.99], [113, 49775.0, 6360.5556, 0.44999999999999996], [146, 49734.1667, 6319.4444, 1.45], [243, 49867.7778, 6239.4444, 0.6699999999999999], [265, 49900.0, 6209.1667, 0.48], [271, 49716.6667, 6183.3333, 0.9], [308, 49790.0, 6388.3333, 0.6799999999999999], [380, 49883.8889, 6258.0556, 0.15999999999999998], [387, 49741.6667, 6427.7778, 1.24], [393, 49668.6111, 6142.2222, 1.12], [398, 49762.5, 6241.3889, 0.89], [437, 49866.9444, 6182.5, 0.94], [453, 49739.7222, 6187.2222, 0.61], [459, 49883.3333, 6166.6667, 1.98], [511, 49853.6111, 6319.1667, 0.24], [528, 49866.6667, 6183.3333, 0.12], [534, 49758.0556, 6478.6111, 1.19], [550, 49706.6667, 6340.5556, 0.45999999999999996], [569, 49683.0556, 6141.6667, 0.13], [584, 49860.2778, 6288.0556, 0.21999999999999997], [621, 49756.3889, 6160.8333, 0.24], [624, 49744.1667, 6328.3333, 0.51]]
#print ("data ", custlist)
#custlist124 = [[124, 49955.8333, 5924.7222, 0.0], [14, 49968.8889, 5931.9444, 0.32999999999999996], [36, 49972.7778, 5941.9444, 0.81], [63, 49916.6667, 5783.3333, 0.47], [105, 49933.0556, 6063.6111, 1.27], [118, 50099.4444, 5997.5, 0.71], [130, 49866.9444, 5773.3333, 1.19], [147, 49916.9444, 6011.9444, 0.8500000000000001], [160, 49830.8333, 5845.0, 0.91], [169, 49994.4444, 6013.0556, 1.4], [171, 49916.6667, 6000.0, 1.3199999999999998], [177, 50107.2222, 6007.7778, 1.23], [204, 49979.7222, 5910.8333, 0.69], [206, 49947.5, 5979.1667, 0.88], [210, 49933.3333, 6066.6667, 0.47], [214, 49855.5556, 6047.2222, 1.6099999999999999], [220, 49877.5, 5887.2222, 0.61], [245, 49866.6667, 5833.3333, 0.15000000000000002], [254, 49962.5, 5981.6667, 1.28], [260, 49923.3333, 5872.2222, 1.62], [264, 49930.8333, 6037.2222, 0.8600000000000001], [324, 50069.4444, 6070.5556, 0.42000000000000004], [362, 50164.7222, 6015.0, 0.75], [372, 49985.0, 6073.3333, 1.75], [397, 49888.8889, 5978.8889, 0.7], [408, 50108.0556, 5923.3333, 0.28], [411, 49984.4444, 5872.5, 0.99], [418, 49853.0556, 5915.8333, 0.32999999999999996], [446, 49814.1667, 5874.7222, 0.94], [449, 49899.1667, 5812.7778, 1.74], [476, 49886.1111, 5936.6667, 0.31000000000000005], [507, 49970.0, 5837.2222, 1.15], [539, 49900.8333, 5858.6111, 0.28], [542, 49933.8889, 5941.9444, 0.47], [566, 49851.6667, 5793.3333, 0.26], [606, 50165.5556, 6088.8889, 1.44], [633, 49923.0556, 5878.6111, 0.18000000000000005]]


# print "VehicleCap: ",data["vehicleCapacity"]
# print "Depot: ",data["depot"]["x"],":",data["depot"]["y"]
# print "Sample Node: ",data["nodes"][0]["x"],":",data["nodes"][0]["y"],"-->",data["nodes"][0]["demand"]
#def buildSavings():
    #after this customers will have x:val , y:val,demand:val

noOfCustomers523 = len(custlist523)
print (noOfCustomers523)
customerPositionDemand = dict()
vehicleCap = 14
print (vehicleCap)
for i in range(1,noOfCustomers523):
    temp = []
    temp = itemgetter(i)(custlist523)
    print (temp)
    xloc = temp [1]
    yloc = temp [2]
    demand = temp [3]
    customerPositionDemand[xloc,yloc] = demand

    
#def distDepot


#calculating savingss for all pairs
savings = dict()
customerPositions =  list(customerPositionDemand)
print(customerPositions)
pointsLen = len(customerPositions)
print (pointsLen)

#depot = dict()
temp = itemgetter(0)(custlist523)
# print ('temp---',temp)
xlocdepot = temp [1]
ylocdepot = temp [2]
demand = 0
depot = (xlocdepot,ylocdepot)
# print ('temp data---',temp)
#depot [xlocdepot,ylocdepot] = demand
#----------------------------------------------------------------#

#Step 1
                            
distanceDict = dict()
for i in range(pointsLen):
    for j in range(i+1,pointsLen):
        distanceDict[(customerPositions[i], customerPositions[j])] = euclideanDistance(customerPositions[i], customerPositions[j])

#Step 2
for i in range(pointsLen):
    for j in range(i+1,pointsLen):
        savings[(customerPositions[i], customerPositions[j])] = computeSaving(depot,customerPositions[i], customerPositions[j])
savings = sorted(savings.items(),key=operator.itemgetter(1),reverse=True)
l = len(savings)
cust_pairs = list()
for i in range(l):
    cust_pairs.append(savings[i][0])


#initially none of the customers have been isServed
customerServed = dict()
for c in customerPositions:
    customerServed[c] = False


#Step 3
def inPrevious(new,existing):
    start = existing[0]
    end = existing[len(existing)-1]
    if new == start:
        return 1
    elif new == end:
        return 0
    else:
        return -1
     
routes = dict()
l = len(cust_pairs)
i = 0
idx = -1
truck = [0,0,0,0,0]

# step 4
while (not(allCustomersConsidered(customerServed))):
    #choosing the maximum savings customers who are unserved
    for c in cust_pairs:
        if (isServed(c[0]) == False and isServed(c[1]) == False):
            hasBeenServed(c[0])
            hasBeenServed(c[1])
            idx += 1
            routes[idx] = ([c[0],c[1]]) 
            break
        
    #finding a cust that is either at the start or end of previous route
    for c in cust_pairs:
        res = inPrevious(c[0], routes[idx])
        if res == 0 and capacityValid(routes[idx], c[1]) and (isServed(c[1]) == False):
            if c[1] == (49460.8333,6033.0556):
                print (customerServed[c[1]])
            hasBeenServed(c[1])
            routes[idx].append(c[1]) 
        elif res == 1 and capacityValid(routes[idx], c[1]) and (isServed(c[1]) == False):
            if c[1] == (49460.8333,6033.0556):
                print (customerServed[c[1]])
            hasBeenServed(c[1])
            routes[idx].insert(0,c[1])
        
        else:
            res = inPrevious(c[1], routes[idx])
            if res == 0 and capacityValid(routes[idx], c[0]) and (isServed(c[0]) == False):
                if c[0] == (49460.8333,6033.0556):
                    print (customerServed[c[0]])
                hasBeenServed(c[0])
                routes[idx].append(c[0]) 
            elif res == 1 and capacityValid(routes[idx], c[0]) and (isServed(c[0]) == False):
                if c[0] == (49460.8333,6033.0556):
                    print (customerServed[c[0]])
                hasBeenServed(c[0])
                routes[idx].insert(0,c[0])


# step 5
for point in customerPositionDemand.keys():
    print (point)

for r in routes.values():
    for routeValues in r:
        print (routeValues)

# printing each load
capAfterServingCust = []
vehicleCap1 = vehicleCap

for r in routes.values():
    cap = 0
    print("route", r)
    for points in r:
        cap = customerPositionDemand[points]
        vehicleCap1 = vehicleCap1 - cap
        capAfterServingCust.append(vehicleCap1)
   

capAfterServingCust.insert(0,vehicleCap)


for r in routes.values():
    cap = 0
    
    for points in r:
        
        cap += customerPositionDemand[points]
    

# step 6
#adding depot at ends
for r in routes.values():
    addDepotAtEnds(depot, r)


totalDist = 0
for k,v in routes.items():
    totalDist += calculateRouteCost(v,capAfterServingCust)
    print ("Route",k,"-",v)
print (totalDist)

