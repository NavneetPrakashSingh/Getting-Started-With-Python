# -*- coding: utf-8 -*-
"""
Created on Thu Mar 29 11:14:16 2018

@author: Navneet
"""
from decimal import *
#python string formatting | https://www.hackerrank.com/challenges/python-string-formatting/problem
count = int(input())
for i in range(1, count+1):
    decimalValue =int(Decimal(i))
    octaValue = oct(i)
    hexadecimalValue = hex(i)
    binaryValue = bin(i)
    binaryLength = len(binaryValue)    
   # print(decimalValue,"--",octaValue,"--",hexadecimalValue,"--",binaryValue)
    print(decimalValue,ljust(binaryLength),octaValue,ljust(binaryLength),hexadecimalValue,ljust(binaryLength),binaryValue)
    