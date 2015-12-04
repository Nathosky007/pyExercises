'''
Created on 5 Nov 2015

@author: SainathVasudev_M
'''
import itertools

file1 = open('data.txt','w')

file1.write('first line of data goes here!\n')

file1.write('second line of data\n')

file1.close()

file1 = open(r"C:\Users\sainathvasudev_m\workspace\Testing\Capitals.txt")

#print(file1.read())

N=10

for line in itertools.islice(file1,N):
    print(line)
# print("***************Demarkation*************")