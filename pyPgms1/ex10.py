'''
Created on 27 Jan 2016

@author: SainathVasudev_M
'''

tabby_cat = "\vI'm tabbed in"
persian_cat = "I'm split\non a \bline."
backslash_cat = "I'm \\ a \\ cat."

fat_cat = """
a list:
\t* food
\t* fuel
\t* cash
"""

print tabby_cat
print persian_cat
print backslash_cat
print fat_cat

while True:
    for i in ["/","-","|","\\","|"]:
        print "%s\r" % i