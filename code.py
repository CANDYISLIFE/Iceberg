boatSize = input("What size boat are you renting? Say L, M, or S ")
speed = int(input("How fast are you traveling? "))

if boatSize == str("L"):
    beginningSize = 10000000
    rental = 1400
if boatSize == str("M"):
    beginningSize = 100000
    rental = 780
if boatSize == str("S"):
    beginningSize = 500000
    rental = 520
else:
    print("Please enter either a L, M, or S ")

days = 9600/(speed*24)
#print(days)

radius = ((beginningSize*3)/(4*3.14159265))**(1/3)
#print(radius)

for i in range(days):
    
    