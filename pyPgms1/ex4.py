'''
Created on 25 Jan 2016

@author: SainathVasudev_M
'''

cars = 100
space_in_a_car = 4
drivers = 30
passengers = 90

cars_not_driven = cars - drivers
cars_driven = drivers
carpool_capacity = cars_driven * space_in_a_car
avg_psngr_per_car = passengers / cars_driven

print "There are ", cars , "cars available."
print "There are only ", drivers, "drivers available."
print "There will be ", cars_not_driven, "empty cars today."
print "We can transport ", carpool_capacity, "people today"
print "We have ", passengers, "to cagrpool today."
print "We have to put about ", avg_psngr_per_car, "in each car."

