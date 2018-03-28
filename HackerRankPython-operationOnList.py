# -*- coding: utf-8 -*-
"""
Created on Mon Mar 26 22:53:11 2018

@author: Navneet
"""

#opeartions on list | https://www.hackerrank.com/challenges/python-lists/problem
n = int(input())
requiredList=[]
for i in range(0, n):
    inputCommand = input()
    opeartion = inputCommand.split(' ')
    command = opeartion[0]
    if(command =="insert"):
        index = opeartion[1]
        value = opeartion[2]
        requiredList.insert(index,value)
    if(command=="print"):
        print(requiredList)
    if(command=="remove"):
        value = opeartion[1]
        requiredList.remove(value)
    if(command == "append"):
        value = opeartion[2]
        requiredList.append(value)
    if(command="sort"):
        requiredList.sort()
    if(command=="pop"):
        requiredList.pop()
    if(command == "reverse"):
        requiredList.reverse()

    