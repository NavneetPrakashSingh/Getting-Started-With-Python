# -*- coding: utf-8 -*-
"""
Created on Thu Mar 29 13:41:42 2018

@author: Navneet
"""

#capitalize string | https://www.hackerrank.com/challenges/capitalize/problem
def capitalize(string):
    splitString = string.split(' ')
    returningString =""    
    for i in range(0,len(splitString)):
        if(i>0):
            returningString = returningString+" "+splitString[i].capitalize()
        else:
            returningString = returningString+splitString[i].capitalize()
    return returningString
    
inputString = input()
returningValue = capitalize(inputString)
print(returningValue)
