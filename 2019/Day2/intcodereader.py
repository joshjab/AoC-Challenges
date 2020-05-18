import csv
import os, sys

opcode = []
#Read csv into an array
with open(os.path.join(sys.path[0], 'input.txt'), 'r') as file:
    opcode = file.read().split(',')

map = map(int, opcode)
opcode = list(map)
#Read the directions..
opcode[1] = 12
opcode[2] = 2

#Loop every 4 values, run commands
count = 0
for i in range(len(opcode)):
    #Iterator
    if(count % 4 == 0 or count == 0):
        count = 0
        #If first value is 1
        if(opcode[i]== 1):
            #Add the two values at 2nd and 3rd positions
            sum = opcode[opcode[i+1]] + opcode[opcode[i+2]]
            #print("(" + str(opcode[opcode[i+1]]) + " + " + str(opcode[opcode[i+2]]) + ") To position: " + str(opcode[i+3]))
            #Move to position of 4th value
            opcode[opcode[i+3]] = sum
        #If 2
        elif(opcode[i] == 2):
            #Multiply the two values at 2nd and 3rd positions
            mult = opcode[opcode[i+1]] * opcode[opcode[i+2]]
            #print("(" + str(opcode[opcode[i+1]]) + " * " + str(opcode[opcode[i+2]]) + ") To position: " + str(opcode[i+3]))
            #Move value to position of 4th value
            opcode[opcode[i+3]] = mult
        elif(opcode[i] == 99):
            print("Opcode 99 detected! Finishing program..")
            break
        #If 99, break loop
        else:
            print("Warning: Unknown opcode at 4th value:" + str(opcode[i]))
        count+=1
    else:
        count+=1
        pass
    
#Output the value left at position 0
print("Position [0]: " + str(opcode[0]))
#print("Full finished code: ")
#count = 0
#for code in opcode :
#    print(str(count) + ": " + str(code) + ", ")
#    count+=1