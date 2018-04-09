# -*- coding: utf-8 -*-
"""
Created on Mon Apr  9 13:48:44 2018

@author: Navneet
"""

#program for insertion sort using python

def insertionSort(unsortedNumberString):
    lengthOfUnsortedString = len(unsortedNumberString)
    for i in range(0, lengthOfUnsortedString):
        for j in range(0,i):
            if(unsortedNumberString[j]>unsortedNumberString[i]):
                temp = unsortedNumberString[j]
                unsortedNumberString[j] = unsortedNumberString[i]
                unsortedNumberString[i] = temp
    print(unsortedNumberString)
    
    
print("Enter the unsorted numbers to be sorted")
unsortedNumberString = input().split(' ')
insertionSort(unsortedNumberString)
