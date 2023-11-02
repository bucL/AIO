inputfile = open("elecin.txt", 'r')
outputfile = open("elecout.txt", 'w')

content = inputfile.readlines()
a = 0
b = 0
c = 0
for i in content[1]:
    if i == "A":
        a +=1
    elif i == "B":
        b+=1
    else:
        c+=1
if a == b or c == b or a == c:
    outputfile.write("T")
else:
    mostvotes = max(a, b, c)
    if mostvotes == a:
        outputfile.write("A")
    elif mostvotes == b:
        outputfile.write("B")
    else:
        outputfile.write("C")