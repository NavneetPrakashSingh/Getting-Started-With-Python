# -*- coding: utf-8 -*-
"""
Created on Mon Mar 19 10:22:03 2018

@author: Navneet
"""

print("Checking if else statement")
n = int(input())
if(n>=2 and n<=5) :
    if(n%2 == 0) :
        print("Not Weird")
elif (n >= 6 and n<=20) :
    if(n%2 == 0) :
        print("Weird")
elif (n>20) :
    if(n%2 == 0) :
        print("Not Weird")