from sys import argv
from os.path import exists

scr, scr_file, target_file = argv

print 'copying from %s to %s ' % (scr_file, target_file)

in1 = open(scr_file)
in_data = in1.read()

print 'Input file is %d bytes long ' % len(in_data)

print 'check if output file exists %r' % exists(target_file)
print 'RETURN to continue \n CTRL-C to abort'
raw_input()

out2 = open(target_file,'w')
out2.write(in_data)

print 'copy process if finished'

#out2.close()
in1.close()