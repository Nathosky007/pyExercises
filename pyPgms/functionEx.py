'''
Created on 26 Nov 2015

@author: SainathVasudev_M
'''
def distance_from_zero(args1):
    if (type(args1) == int or type(args1) == float):
        print "from if block"
        return abs(args1)
    
    else:
        print "from else block"
        print type(args1)
        return "Nope"
    
print (distance_from_zero(-120))

print (type(30))

def plane_ride_cost(city):
    if (city == 'Charlotte'):
        return 183
    elif (city == "Tampa"):
        return 220
    elif (city == "Pittsburgh"):
        return 222
    elif (city == "Los Angeles"):
        return 475
    
print(plane_ride_cost("Charlotte"))