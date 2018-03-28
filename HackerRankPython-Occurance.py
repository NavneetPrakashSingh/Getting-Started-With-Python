# -*- coding: utf-8 -*-
"""
Created on Wed Mar 28 07:49:13 2018

@author: Navneet
"""

#find the occurance of substring within a string | https://www.hackerrank.com/challenges/find-a-string/problem
def countSubstring(string, subString):
    finalCount = 0
    for i in range(0,len(string)):
        if(string[i:i+len(subString)] == subString):
            finalCount = finalCount+1
            print("in finalCount")
    return finalCount
    
string = input().split()
subString = input().split()
count =countSubstring(string,subString)
print(count)