'''
Created on 30 Nov 2015

@author: SainathVasudev_M
'''


def hotel_cost(nights):
    return 140 * nights
    
def plane_ride_cost(city):
    if (city == "Charlotte"):
        return 183
    elif (city == "Tampa"):
        return 220
    elif (city == "Pittsburgh"):
        return 222
    elif (city == "Los Angeles"):
        return 475
        
def rental_car_cost(days):
    day_cost = 40 * days
     
    if (days >= 7):
        return day_cost - 50
    elif(days >= 3):
        return day_cost - 20
    else:
        return day_cost
    
def trip_cost(city, days,spending_money):
    return hotel_cost(days) + plane_ride_cost(city) + rental_car_cost(days) + spending_money

final_cost = trip_cost("Los Angeles", 15, 600)

print "the final_cost of the trip is " + str(final_cost)
        
    
