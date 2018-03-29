# -*- coding: utf-8 -*-
"""
Created on Thu Mar 29 09:28:56 2018

@author: Navneet
"""

#wrap string around width | https://www.hackerrank.com/challenges/text-wrap/problem
import textwrap
def wrap(string, maxWidth):    
    return textwrap.fill(string,maxWidth)

string , maxWidth = input(), int(input())
result = wrap(string, maxWidth)
print(result)