# -*- coding: utf-8 -*-
"""
Created on Tue Aug 17 17:36:42 2021

@author: lenovo
"""

num=input('please input a number: ')
num=int(num)
if num%4==0:
    print(str(num) +' is the number of 4')
elif num%2==0:
    print(str(num) +' is even')
else:
    print(str(num) +' is odd')
        