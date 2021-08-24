# -*- coding: utf-8 -*-
"""
Created on Tue Aug 17 18:26:09 2021

@author: lenovo
"""

a=[1,4,9,16,25,36,49,64,81,100]
length=len(a)
even_a=[]
for i in range(length):
    if a[i]%2==0:
        even_a.append(a[i])
print(str(even_a) +' only have the even elements of a')
        