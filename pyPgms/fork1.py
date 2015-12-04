'''
Created on 6 Nov 2015

@author: sainathvasudev_m
'''
import os
##from os import fork

def child():
    print("hello from child", os.getpid())
    os._exit(0)
    
def parent():
    while True:
        newpid = os.fork()
        if newpid == 0:
            child()
        else:
            print("hello from parent", os.getpid(), newpid)
        if input() == 'q': break
        
parent()