# -*- coding: utf-8 -*-
"""
Created on Thu Mar 11 09:58:18 2021

@author: Victoria
"""

for i in range(1,8,2):
    if i < 3:
     print(" "*(4-i),"*"*i)
    if i >= 3 and i <5 :
     print(" "*(5-i),"*"*i)
    if i >= 5 and i <7 :
     print(" "*(6-i),"*"*i)
    if i >= 7 :
     print(" "*(7-i),"*"*i)
        
        
for i in range(5,0,-2):
    
    if i >= 5 and i <7 :
     print(" "*(6-i),"*"*i)
    if i >= 3 and i <5 :
     print(" "*(5-i),"*"*i)
    if i <3 :
     print(" "*(4-i),"*"*i)
    
    
    