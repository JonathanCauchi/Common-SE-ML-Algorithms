#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Feb 13 14:16:20 2020

@author: joncauchi
"""


list = [3,2,7,5,9,6,1]
 
for i in range(len(list)):
    
    location = i
    for j in range(i+1, len(list)):
        
        if(list[location] > list[j]):
            location = j
        
        elif(list[location]< list[j]):
            pass #do nothing
            
    #swap
    temp = list[i]
    list[i] = list[location]
    list[location] = temp
    
for c in list:
    print(c)