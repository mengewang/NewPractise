# -*- coding: utf-8 -*-
"""
Created on Tue Aug 17 17:43:49 2021

@author: lenovo
"""

num=input('please give us a number:')
num=int(num)
new_list=[]
origin_list=[1,1,2,3,4,8,13,21,34,55,89]
for element in origin_list:
    if element<num:
        new_list.append(element)
print(str(new_list) +' contains only elements that are smaller than '+ str(num))