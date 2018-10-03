import math

boatSize = input("What size boat are you renting? Say L, M, or S ")
speed = int(input("How fast are you traveling? Enter 1, 3, or 5 "))
distance = 0

if boatSize == str("L"):
    beginningSize = 10000000
    rental = 1400
    #fuelCost = (2.01947*math.log(beginningSize)-6.86667)
    #print(fuelCost)
if boatSize == str("M"):
    beginningSize = 1000000
    rental = 780
    #fuelCost = (1.69375*math.log(beginningSize)-5.8)
    #print(fuelCost)
if boatSize == str("S"):
    beginningSize = 500000
    rental = 520
    #fuelCost = (1.36803*math.log(beginningSize)-4.86667)
    #print(fuelCost)
#else:
    print("Please enter either a L, M, or S ")

"""
if speed == 5:
    fuelCost = (1.84575*math.log(beginningSize)-4.0333)7
    print(fuelCost)
if speed == 3: 
    fuelCost = (1.52003*math.log(beginningSize)-3.46667)
    print(fuelCost)
if speed == 1: 
    fuelCost = (1.19431*math.log(beginningSize)-2.83333)
    print(fuelCost)
"""

days = 9600/(speed*24)
#print(days)

radius = ((beginningSize*3)/(4*3.14159265))**(1/3)
#print(radius)
beginningSize = radius
#print(beginningSize)

for i in range(int(days)):
    if speed == 5:
        fuelCost = (1.84575*math.log(beginningSize)-4.0333)
        shrink = .0001(beginningSize) 
        #print(fuelCost)
    if speed == 3: 
        fuelCost = (1.52003*math.log(beginningSize)-3.46667)
        shrink = .00008(beginningSize)
        #print(fuelCost)
    if speed == 1: 
        fuelCost = (1.19431*math.log(beginningSize)-2.83333)
        shrink = .00006(beginningSize)
        #print(fuelCost)
    distance += (speed*24)
    beginningSize += -shrink
    print(beginningSize)
        
        
        
        
        
        
        
    