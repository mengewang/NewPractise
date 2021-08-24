# -*- coding: utf-8 -*-
"""
Created on Tue Aug 17 17:52:15 2021

@author: lenovo
"""

num=input('please input a number:')
num=int(num)
list_of_div=[]
for i in range(1,num+1):
    if num%i==0:
        list_of_div.append(i)
print(str(list_of_div) +'is the list of all the divisors of '+ str(num))        
    