# -*- coding: utf-8 -*-
"""
Created on Tue Aug 17 18:00:22 2021

@author: lenovo
"""

a=[1,1,2,3,5,8,13,21,34,55,89]
b=[1,2,3,4,5,6,7,8,9,10,11,12,13]
com_list=[]
for i in a:
    if i in b:
        if i not in com_list:
            com_list.append(i)
print(str(com_list) +' contains only the elements that are comman between the lists.')
    