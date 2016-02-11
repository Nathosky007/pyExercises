from sys import argv

scr, f_name = argv

print 'we are going to erase %r' % f_name
print 'if you want to cancel the operation, hit Ctrl-C (^C)'
print 'if you want to proceed with operation , hit RETURN'

raw_input("?")

print 'Opening file...'
target = open(f_name, 'w')

print 'Truncating the file '
target.truncate()

print 'Please enter 3 lines'

line1 = raw_input("line 1:")
line2 = raw_input("line 2:")
line3 = raw_input("line 3:")

print 'Writing these 3 lines to the file.'

target.write(('%r \n%r \n%r \n' % (line1,line2,line3) ))
'''target.write('\n')
target.write(line2)
target.write('\n')
target.write(line3)
target.write('\n')
'''
print 'file contents saved, below is the newly formed file '
target.close()

target1 = open(f_name)
print target1.read()
target1.close()