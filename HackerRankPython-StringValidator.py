# -*- coding: utf-8 -*-
"""
Created on Wed Mar 28 08:00:06 2018

@author: Navneet
"""

#string validator | https://www.hackerrank.com/challenges/string-validators/problem
s =input()
listOfS = list(s)
upperCountValue = 0
lowerCountValue = 0
alphaNumericCountValue = 0
alphabeticCountValue = 0
digitCountValue = 0
for i in listOfS:
    if(i.isupper()):
        upperCountValue = 1
        break
    else:
        upperCountValue = 0
        
for i in listOfS:
    if(i.islower()):
        lowerCountValue = 1
        break
    else:
        lowerCountValue = 0
        
for i in listOfS:
    if(i.isalnum()):
        alphaNumericCountValue = 1
        break
    else:
        alphaNumericCountValue = 0
        
for i in listOfS:
    if(i.islower()):
        alphabeticCountValue = 1
        break
    else:
        alphabeticCountValue = 0
        
for i in listOfS:
    if(i.isdigit()):
        digitCountValue = 1
    else:
        digitCountValue = 0
        
if(alphaNumericCountValue):
    print("True")
else:
    print("False")
    
if(alphabeticCountValue):
    print("True")
else:
    print("False")
if(digitCountValue):
    print("True")
else:
    print("False")
if(lowerCountValue):
    print("True")
else:
    print("False")
if(upperCountValue):
    print("True")
else:
    print("False")