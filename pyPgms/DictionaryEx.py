'''
Created on 30 Nov 2015

@author: SainathVasudev_M
'''
inventory = {
    'gold' : 500,
    'pouch' : ['flint', 'twine', 'gemstone'], # Assigned a new list to 'pouch' key
    
    'backpack' : ['xylophone','dagger', 'bedroll','bread loaf']
}

# Adding a key 'burlap bag' and assigning a list to it
inventory['burlap bag'] = ['apple', 'small ruby', 'three-toed sloth']

print "the current contents of dictionary is " + str(inventory)

# Sorting the list found under the key 'pouch'
inventory['pouch'].sort() 

print "the current contents of dictionary is " + str(inventory)
inventory['pocket'] = ['seashell','strange berry','lint']
inventory['pocket'].sort()
print "the current contents of dictionary is " + str(inventory)

inventory['backpack'].remove('dagger')
print "the current contents of dictionary is " + str(inventory)


