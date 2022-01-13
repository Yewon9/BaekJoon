# -*- coding: utf-8 -*-
"""
Created on Thu Jan 13 14:25:02 2022

@author: laura
"""

A,B,C= input().split()
A = int(A)
B = int(B)
C = int(C)

print((A+B)%C)
print(((A%C)+(B%C))%C)
print((A*B)%C)
print(((A%C)*(B%C))%C)