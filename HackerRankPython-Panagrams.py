# -*- coding: utf-8 -*-
"""
Created on Thu Apr 12 16:16:26 2018

@author: Navneet
"""

#panagram test | https://www.hackerrank.com/challenges/pangrams/problem

def removeDublicateValues(s):
    return "".join(set(s))

def panagrams(s):
    #panagarm logic starts here
    #lowerString = s.lower()
    stringWithoutSpace = s.replace(" ","").lower()
    stringWithoutSpaces = removeDublicateValues(stringWithoutSpace)
    print(stringWithoutSpaces)
    #print(stringWithoutSpaces)
    sum = 0
    for values in stringWithoutSpaces:
        sum = sum + ord(values)
        print(sum)
    if(sum == 2847):
        return "pangram"
    else:
        return "not pangram"

inputString = input()
returningValue = panagrams(inputString)
print(returningValue)