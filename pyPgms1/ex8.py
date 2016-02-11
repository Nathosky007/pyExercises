'''
Created on 26 Jan 2016

@author: SainathVasudev_M
'''

formatter = "%r %r %r %r"

print formatter % (1, 2, 3, 4)
print formatter % ("one", "two", "three", "four")
print formatter % ("True", "False","True", "False")
print formatter % (formatter, formatter, formatter, formatter)
print formatter % (
    "this is string1.",
    "the string1 is a mixed bag.",
    "A mixed bag's of characters,",
    "and special characters too")