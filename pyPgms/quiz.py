#!/usr/local/bin/python
nums = set([1,1,2,3,3,3,4])
print len(nums)

x = True
y = False
z = False

if not x or y:
    print 1
elif not x or not y and z:
    print 2
elif not x or y or not y and x:
    print 3
else:
    print 4
