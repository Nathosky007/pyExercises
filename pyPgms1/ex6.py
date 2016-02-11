'''
Created on 26 Jan 2016

@author: SainathVasudev_M
'''
x = "there are %d types of people." % 10
binary = 'binary'
do_not = 'don\'t'

y = 'those who know %s and those who %s.' % (binary, do_not)

print x
print y

print "I said: %r." % x
print 'i also said: \'%s\'.' % y

hilarious = False
joke_eval = "Isn't the joke so funny ? %r"

print joke_eval % hilarious

w = "LHS of "
e = "a string with RHS"

print w + e
