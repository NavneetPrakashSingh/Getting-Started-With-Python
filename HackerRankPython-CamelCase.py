# -*- coding: utf-8 -*-
"""
Created on Mon Apr  2 14:57:32 2018

@author: Navneet
"""

#camelcaseing | https://www.hackerrank.com/challenges/camelcase/problem
stringValue ='singleword'
count = 0
for i in stringValue:
    if(i.isupper()):
        count = count + 1
if count == 0:
    print(0)
else:
    print(count + 1)
        