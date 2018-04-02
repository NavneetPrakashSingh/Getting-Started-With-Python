# -*- coding: utf-8 -*-
"""
Created on Mon Apr  2 18:59:00 2018

@author: Navneet
"""

#caesar cipher | https://www.hackerrank.com/challenges/caesar-cipher-1/problem


def caesarCipher(s, k):
    finalString = ""
    for i in s:
        print("ord of i is",ord(i))
        finalChar = (ord(i) + k)%26
        print(finalChar)
        finalString = finalString+chr(finalChar)
    print(finalString)        
    return "reached here"

if __name__ == "__main__":
    n = int(input().strip())
    s = input().strip()
    k = int(input().strip())
    result = caesarCipher(s, k)
    print(result)
