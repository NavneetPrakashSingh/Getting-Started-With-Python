# -*- coding: utf-8 -*-
"""
Created on Sat Apr  7 14:16:58 2018

@author: Navneet
"""

#operations on queue using python
#queue works on FIFO principle i.e added from last and removed from first
from collections import deque
listValue = ['list1','list2','list3','list4']
queue = deque(listValue)
queue.append("list5")
print(queue)
queue.popleft()
print(queue)
