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
    avg = (scores[0] + scores[1] + scores[2])/3
    student_marks[name] = avg
    
query_name = input()
print("%.2f" % round(student_marks[query_name],2))

