beginningSize = int(input("How big is the iceberg at first? "))
speed = int(input("How fast are you traveling? "))

days = 9600/(speed*24)
#print(days)

radius = ((beginningSize*3)/(4*3.14159265))**(1/3)
#print(radius)

for i in range(days):
    