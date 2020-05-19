import math
import os, sys

def fuel_calc(mass):
    
    fuel = math.floor(int(mass)/3) - 2
    if (fuel <= 0):
        return 0
    else:
        #print (str(fuel) + " + " + str((fuel_calc(fuel))))
        return fuel + (fuel_calc(fuel))

#Read all lines in file, append to array
input = open(os.path.join(sys.path[0], "input.txt"), 'r')
modules = input.readlines()

fuel_reqs = []
#In each module
count = 0
for module in modules:
    #Divide mass by 3, round down, and subtract 2
    #Append to new array
    fuel_reqs.append(fuel_calc(module))
    #print("Module " + str(count) + ": " + str(fuel_calc(module)))
    count+=1
   
#Add all values of array
fuel_sum = sum(fuel_reqs)
#Print value
print("The total fuel required is: " + str(fuel_sum))
