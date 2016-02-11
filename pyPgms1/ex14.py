from sys import argv

script, u_name = argv
prompt = '@@ '

print "Hi %s, I am in %s script " % (u_name, script)
print 'Few questions for you'
print 'Do you like me %s ' % u_name
likes = raw_input(prompt)

print 'where do you live %s? ' % u_name
lives = raw_input(prompt)

print 'Your computer? '
comp = raw_input(prompt)

print """
So you said %r about liking me.
Your residence is in %r.
You have a machine %r.
""" % (likes, lives, comp)