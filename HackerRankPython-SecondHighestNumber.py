# -*- coding: utf-8 -*-
"""
Created on Mon Mar 26 09:41:48 2018

@author: Navneet
"""

#second max number in a list using python | https://www.hackerrank.com/challenges/find-second-maximum-number-in-a-list/problem
n = int(input())
ar = map(int, input().split())
currentList = list(ar)
currentList.sort()
max = currentList[n-1]
for i in reversed(currentList):
    if (i<max):
        max = i
        break
print(max)
    