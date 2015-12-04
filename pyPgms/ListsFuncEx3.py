'''
Created on 4 Dec 2015

@author: SainathVasudev_M
'''
n = [1, 3, 5, 7, 10, 12, 13]
# Do your multiplication here
print "removing items from list by different methods"

print "1 <list>.pop(index)\n" , "deletes the element at the index specified and returns the index"
print "2 <list>.remove(item)\n" , "deletes the element after searching for the element specified in remove arg"
print "3 del(<list>[index])\n" ,"removes the item at given index, returns null "

print
print

print "the original list is\n " , n

n.pop(0)
print "the new list after pop operation is \n " , n

n.remove(12)
print "the modified list after removing of element 12 from the new list \n ", n

del(n[3])
print "the modified list after removing of element at index 3 from the modified list \n ", n
