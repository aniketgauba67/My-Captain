# -*- coding: utf-8 -*-
"""
Created on Thu Jun 24 02:16:51 2021

@author: admin
"""

# Positive Numbers in a Range
List1=[]
n=int(input("Enter no of Elements you want in a List:"))
for i in range(n):
    Value=int(input("Enter the integers in the List"))
    List1.append(Value)
print(List1)
Positive=[]
for j in List1:
    if j>=0:
        Positive.append(j)
print(Positive)