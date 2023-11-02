import sys
sys.setrecursionlimit(1000000000)


# N is the number of instructions.
N = None

# instructions contains the sequence of instructions.
instructions = None

# Open the input and output files.
input_file = open("telein.txt", "r")
output_file = open("teleout.txt", "w")

# Read the value of N and the instructions from the input file.
N = int(input_file.readline().strip())
instructions = input_file.readline().strip()
furthesthouse = 0
totalleft = 0
totalright = 0
for i in instructions:
    if i == 'L':
        totalleft+=1
    else:
        totalright +=1
furthesthouse = max(totalleft, totalright)
if furthesthouse == totalleft:
    if furthesthouse - totalright > 0:
        answer = furthesthouse + 1
    else:
        answer = totalright+1
else:
    if furthesthouse - totalleft > 0:
        answer = furthesthouse + 1
    else:
        answer = totalleft+1


print(answer)
# Write the answer to the output file.
output_file.write("%d\n" % (answer))

# Finally, close the input/output files.
input_file.close()
output_file.close()