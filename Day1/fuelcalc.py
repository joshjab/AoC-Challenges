import math
import os, sys

#Read all lines in file, append to array
input = open(os.path.join(sys.path[0], "input.txt"), 'r')
modules = input.readlines()

fuel_reqs = []
#In each module
for module in modules:
    #Divide mass by 3, round down, and subtract 2
     #Append to new array
    fuel_reqs.append(math.floor(int(module)/3)-2)
   
#Add all values of array
fuel_sum = sum(fuel_reqs)
#Print value
print("The total fuel required is: " + str(fuel_sum))