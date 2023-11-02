#!/usr/bin/env python
import sys
sys.setrecursionlimit(1000000000)

#
# Solution Template for Making Bank
# 
# Australian Informatics Olympiad 2023
# 
# This file is provided to assist with reading and writing of the input
# files for the problem. You may modify this file however you wish, or
# you may choose not to use this file at all.
#

# N is the number of days.
N = None

# days contains the type of each day.
days = None

# Open the input and output files.
input_file = open("bankin.txt", "r")
output_file = open("bankout.txt", "w")

# Read the value of N and the string of characters from the input file.
N = int(input_file.readline().strip())
days = input_file.readline().strip()

# TODO: This is where you should compute your solution. Store the most money
# that you can retire with into the variable answer.

answer = None

if N == 1:
    answer=1
elif N%2 != 0:
    answer = (1+(N/2)-0.5)*((N/2)+0.5)
else:
    answer = (1+(N/2))*N/2

# Write the answer to the output file.
output_file.write("%d\n" % (answer))

# Finally, close the input/output files.
input_file.close()
output_file.close()
