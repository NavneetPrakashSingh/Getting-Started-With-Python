# -*- coding: utf-8 -*-
"""
Created on Fri Mar 23 14:50:23 2018

@author: Navneet
"""

#list in python
x=['navneet','23','India']
for i in x:
    print(i)
    
#append elements to list
for i in x:
    if i == '23':
        x.append("212")

#insert element in list
x.insert(1,"Navneet")

#reverse a list 
#print(list.reverse(x))

#dictionary in python
x_dict = {'First':1,'Second':2,'Third':3}
print(x_dict)
print(x_dict['Third'])
