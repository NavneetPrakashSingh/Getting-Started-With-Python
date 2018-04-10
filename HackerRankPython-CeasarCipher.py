# -*- coding: utf-8 -*-
"""
Created on Mon Apr  2 18:59:00 2018

@author: Navneet
"""

#caesar cipher | https://www.hackerrank.com/challenges/caesar-cipher-1/problem


def caesarCipher(s, k):
    finalString = ""
    characterValues = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
    upperValue = "false"
    for i in s:   
        if(i.isupper()):
            upperValue = "true"
            currentValue = i.lower()
            
        else:
            currentValue = i
            
        if currentValue in characterValues:            
            characterIndex = characterValues.index(currentValue) + 1            
            finalChar = (characterIndex + k)%26      
            
            if(upperValue == "true"):
                finalString = finalString+characterValues[finalChar-1].upper()
                
                upperValue = "false"
            else:                
                finalString = finalString+characterValues[finalChar-1]            
        else:
            finalString = finalString+currentValue
        
    return finalString

if __name__ == "__main__":
    n = int(input().strip())
    s = input().strip()
    k = int(input().strip())
    result = caesarCipher(s, k)
    print(result)
