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

# TODO: This is where you should compute your solution. Store the number of
originalhouse = 0
movedleft = 0
movedright=0
maxleft = [int()]
maxright = [int()]

print(instructions)
for i in instructions:
    if i == "L":
        movedleft+=1
        maxleft.append(movedleft)
    elif i == "R":
        movedright += 1
        maxright.append(movedright)
print("most left", max(maxleft))
print("most right", max(maxright))
print("moved this many left",movedleft)
print("moved htis many right", movedright)

if max(maxleft) == max(maxright):
    answer = movedleft + 1

elif movedright > movedleft:
        answer = (max(maxright)-max(maxleft))+movedleft+1
elif max(maxleft) > max(maxright):
    answer = (max(maxleft) - max(maxright)) + movedright + 1


print(answer)
# Write the answer to the output file.
output_file.write("%d\n" % (answer))

# Finally, close the input/output files.
input_file.close()
output_file.close()