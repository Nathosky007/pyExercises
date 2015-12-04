
#file1 = open('addition_input.txt','r')

#print file1.read()

lines = [line.rstrip('\n') for line in open('addition_input.txt')]
print lines

i = 0
num = len(lines)

while i < num:
    total = int(lines[0])
    total += int(lines[i])
    #print int(lines[i])
    i += 1

print "\n" , total

print type(lines[0])  
    
#print "the sum is " + str(list_index1)