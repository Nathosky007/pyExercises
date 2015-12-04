'''
Created on 4 Dec 2015

@author: SainathVasudev_M
'''
#from testing1 import DictionaryEx2
from testing1.DictionaryEx2 import average

jack ={
       "name" : "Jack",
       "emp_id" : "1023",
       "offices" : ["san jose","new york","london"],
       "ratings" : [78.0,90.0,95.0,89.0]
       }

carlton ={
       "name" : "Carlton",
       "emp_id" : "1340",
       "offices" : ["london","cape town","beijing"],
       "ratings" : [89.0,80.5,90.0,89.0]
       }

mike ={
       "name" : "Mike",
       "emp_id" : "5143",
       "offices" : ["san diego","dubai","abu dhabi"],
       "ratings" : [45.0,40.0,35.0,45.0]
       }

jared ={
       "name" : "Jared",
       "emp_id" : "7612",
       "offices" : ["rio de janeiro","massachuesetts","muscat"],
       "ratings" : [25.0,34.0,41.0,43.0]
       }

sheldon ={
       "name" : "Sheldon",
       "emp_id" : "7121",
       "offices" : ["shirali","bhatkal","udupi"],
       "ratings" : [77.0,67.0,90.0,89.0]
       }

employees = [jack,carlton,mike,jared,sheldon]

for emp in employees:
    print "the average rating of " , emp["name"] , "is " , average(emp["ratings"])