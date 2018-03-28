# -*- coding: utf-8 -*-
"""
Created on Tue Mar 27 11:12:36 2018

@author: Navneet
"""

#changing case of string | https://www.hackerrank.com/challenges/swap-case/problem
def swap_case(s):
   
   return s.swapcase()

userString = input()
finalString = swap_case(userString)
print(finalString)