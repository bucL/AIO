#!/usr/bin/env python
import sys
sys.setrecursionlimit(1000000000)

#
# Solution Template for Distincto's Raffle
# 
# Australian Informatics Olympiad 2023
# 
# This file is provided to assist with reading and writing of the input
# files for the problem. You may modify this file however you wish, or
# you may choose not to use this file at all.
#

# N is the number of competitors.
N = None

# Competitors all submit a number between 1 and K inclusive.
K = None

# numbers contains the submitted numbers.
numbers = []

# Open the input and output files.
input_file = open("rafflein.txt", "r")
output_file = open("raffleout.txt", "w")

# Read the values of N, K and the submitted numbers from the input file.
input_line = input_file.readline().strip()
N, K = map(int, input_line.split())
input_line = input_file.readline().strip()
numbers = list(map(int, input_line.split()))

# TODO: This is where you should compute your solution. Store the winning
# number, or -1 if there is no winning number, into the variable answer.
print(N)
print(K)
print(numbers)
answers = []
sorted = [int()]
wrongnumbers= [int()]

numbers.sort()
print(numbers)

for i in range(0, len(numbers)):
    if numbers[i] != numbers[(i+1)] and numbers[i] not in wrongnumbers:
        sorted.append(int((numbers[i])))
    else:
        wrongnumbers.append(int(wrongnumbers[i]))
        print(wrongnumbers, "wrong numbers")




#if answers == []:
  #  answer = -1
#answer = min(answers)


# Write the answer to the output file.
# output_file.write("%d\n" % (answer))

# Finally, close the input/output files.
input_file.close()
output_file.close()
