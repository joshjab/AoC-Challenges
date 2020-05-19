import csv
import os, sys

def run_program(noun, verb):

    opcode = []
    with open(os.path.join(sys.path[0], 'input.txt'), 'r') as file:
        opcode = file.read().split(',')

    mapping = map(int, opcode)
    opcode = list(mapping)

    opcode[1] = noun
    opcode[2] = verb

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
                return opcode[0]
                break
            #If 99, break loop
            else:
                print("Warning: Unknown opcode at 4th value:" + str(opcode[i]))
            count+=1
        else:
            count+=1
            pass
    
#Output the value left at position 0
output = 0
noun = 0
verb = 0

while output != 19690720 or (noun >= 99 and verb >= 99):
    verb+=1
    if verb >= 100:
        noun+=1
        verb = 0
    output = run_program(noun, verb)
    print("Noun: " + str(noun) + ", Verb: " + str(verb) + ", Output: " + str(output))
    
    

print("Correct Combination", noun, verb)
print("100 * " + str(noun) + " + " + str(verb) + " = " + str(100*noun+verb))

