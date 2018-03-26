# -*- coding: utf-8 -*-
"""
Created on Mon Mar 26 17:17:19 2018

@author: Navneet
"""

#finding the percentage | https://www.hackerrank.com/challenges/finding-the-percentage/problem
n = int(input())
student_marks = {}
for values in range(n):
    name, *line = input().split()
    scores = list(map(float, line))
    student_marks[name] = scores
query_name = input()
print(student_marks[query_name])
