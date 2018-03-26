# -*- coding: utf-8 -*-
"""
Created on Mon Mar 26 14:37:39 2018

@author: Navneet
"""

#nested list hackerrank | https://www.hackerrank.com/challenges/nested-list/problem
currentList =[]
currentIndex =0
rangeValue = int(input())
for _ in range(rangeValue):
    name = input()
    score = float(input())
    currentList.append([])
    currentList[currentIndex] = [name,score]
    currentIndex = currentIndex+1
currentList.sort(key=lambda x:x[1])
maxElementValue = currentList[rangeValue-1]
maxElement = maxElementValue[1]

for elements in reversed(currentList):     
    if(elements[1] < maxElement):
        maxElement = elements[1]
        

for elements in currentList:
    if(elements[1] == maxElement):
        print(elements[0])
        
    
    