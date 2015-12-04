'''
Created on 30 Nov 2015

@author: SainathVasudev_M
'''
start_list = [5, 3, 1, 2, 4]
square_list = []


for idd in start_list:
    
    #print str(idd)
    square_list.append(idd ** 2)
    

square_list.sort()
print square_list