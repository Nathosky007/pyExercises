from sys import argv
#Uncommented lines 2-9

scr, filename = argv

txt = open(filename)

print 'the contents of file %r: ' % filename
print txt.read()

print 'type the filename again:'
f_again = raw_input("> ")

txt_again = open(f_again)

print txt_again.read()
txt_again.close()
