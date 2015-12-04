'''
Created on 3 Nov 2015

@author: SainathVasudev_M
'''
import sys
import random
import os
from filecmp import cmp

grocery_list = ['ginger', 'creamy soda', 'ginger ale', 'peas', 'bread']

to_do_list = ['wash clothes', 'pay phoneBill', 'buy binoculars']

print(grocery_list)

print(to_do_list)

master_list = [grocery_list , to_do_list]

print(master_list)

grocery_list.append('marshmellows')

print(master_list)

grocery_list.insert(0, "biscuits")

print(master_list)

grocery_list.remove('creamy soda')

print(grocery_list)

grocery_list.sort()

print(grocery_list) 

del grocery_list[1]

print('the short list is ' , '\n' , grocery_list[2:5])

master_list1 = master_list + grocery_list

print("new master list is " , master_list1)

print(grocery_list.count('marshmellows'))

to_do_list.append('ginger')

print(to_do_list)

value1 = any(map(lambda ginger : ginger in master_list,master_list1))

print(value1)


