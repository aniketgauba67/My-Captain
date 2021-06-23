# -*- coding: utf-8 -*-
"""
Created on Thu Jun 24 01:45:32 2021

@author: admin
"""
#Fibonacci numbers
n= int(input("Enter the number"))
x=0
y=1
z=0
print("Fibonacci Series till",n,"is:")
while(z<=n):
    print(z,end=",")
    x=y
    y=z
    z=x+y