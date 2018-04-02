# -*- coding: utf-8 -*-
"""
Created on Fri Mar 30 11:31:38 2018

@author: Navneet
"""
def minimumBribes(q):
    index = 1
    newList=[]
    for values in q:
        newList.append(values-index)
        index = index + 1
    finalSum = 0
    for values in newList:
        if(values>2):
            print("Too chaotic")
            return
        else:
           if(values>0):
               finalSum = finalSum + values
    print(finalSum)

#chaotic queue | https://www.hackerrank.com/challenges/new-year-chaos/problem
t = int(input().strip())
for a0 in range(t):
    n = int(input().strip())
    q = list(map(int, input().strip().split(' ')))    
    minimumBribes(q)