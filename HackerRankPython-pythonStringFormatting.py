# -*- coding: utf-8 -*-
"""
Created on Thu Mar 29 11:14:16 2018

@author: Navneet
"""

#python string formatting | https://www.hackerrank.com/challenges/python-string-formatting/problem
string = 'navneet'
#string.capitalize()

for i in range(1, count+1):      
    width = len("{0:b}".format(i))    
    print("{0:d} {0:{width}o} {0:{width}X} {0:{width}b}".format(i,width=width))
    #print(decimalValue,rjust(binaryLength),octaValue,ljust(binaryLength),hexadecimalValue,ljust(binaryLength),binaryValue)
    