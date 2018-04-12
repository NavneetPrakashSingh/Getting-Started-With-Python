# -*- coding: utf-8 -*-
"""
Created on Thu Apr 12 10:35:29 2018

@author: Navneet
"""

#hackerrank in string | https://www.hackerrank.com/challenges/hackerrank-in-a-string/problem
def hackerrankInString(s):
    # Complete this function
    compareString = "hackerrank"
    if(len(s)<len(compareString)):
        return "NO"
    j=0
    for i in range(0,len(s)-1):
        if(j<len(s) and s[i] == compareString[i]):
            j = j+1
            
    if(j == len(compareString)):
        return "YES"
    else:
        return "NO"
        
    

if __name__ == "__main__":
    q = int(input().strip())
    for a0 in range(q):
        s = input().strip()
        result = hackerrankInString(s)
        print(result)
