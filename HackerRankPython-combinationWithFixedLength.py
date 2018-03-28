# -*- coding: utf-8 -*-
"""
Created on Mon Mar 26 18:02:08 2018

@author: Navneet
"""
from itertools import combinations_with_replacement
#combinations with a fixed length | https://www.hackerrank.com/challenges/itertools-combinations-with-replacement/problem
inputString = input().split()
stringValue = inputString[0]
stringList = list(stringValue)
lengthOfString = inputString[1]
stringList.sort()
#print(stringList)
for elements in combinations_with_replacement(stringList ,int(lengthOfString)):
    print("".join(elements))