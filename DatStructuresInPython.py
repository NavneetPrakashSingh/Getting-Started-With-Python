# -*- coding: utf-8 -*-
"""
Created on Fri Mar 23 12:49:36 2018

@author: Navneet
"""

#data structure in python
stringValue = 'navneet'
anotherStringValue ='singh'
#concatenate a string
print(stringValue+" "+anotherStringValue)
#repeat a string 2 number of times
print(stringValue*2)
#slicing string into different parts
slicedString = stringValue[0:5]
#lower bound is included but upper bound is not included in sliced string
print(slicedString)

#capitalize firt alphabet of the string
print(str.capitalize(stringValue))

#print length of the string
print(len(stringValue))

#replace value within the string
print(stringValue.replace('avneet','eat'))