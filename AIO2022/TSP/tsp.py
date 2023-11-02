inputfile = open('tspin.txt', 'r')
outputfile = open('tspout.txt', 'w')

numbers = []
count = 0
lines = inputfile.readlines()
print(lines[1])
input_string = "1 2 3 4 5"
numbers_list = [int(x) for x in lines[1].split()]

print(numbers_list)