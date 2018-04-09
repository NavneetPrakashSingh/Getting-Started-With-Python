# -*- coding: utf-8 -*-
"""
Created on Mon Apr  9 10:02:06 2018

@author: Navneet
"""

#stack in python
from collections import deque
newList = ["Name 1", "Name 2", "Name 3"]
stack = deque(newList)
stack.pop()
stack.append("navmeet")
print(stack)
