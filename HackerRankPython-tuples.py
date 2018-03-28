# -*- coding: utf-8 -*-
"""
Created on Tue Mar 27 09:46:12 2018

@author: Navneet
"""

#python tuples | https://www.hackerrank.com/challenges/python-tuples/problem
count = int(input())
t = tuple(list(input().split()))

print(hash(t))