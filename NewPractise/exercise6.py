# -*- coding: utf-8 -*-
"""
Created on Tue Aug 17 18:09:11 2021

@author: lenovo
"""

word=input('please input a string: ')
str_num=len(word)
corret=1
for i in range(int(str_num/2)):
    if word[i]!=word[str_num-1-i]:
        corret=0
        break
if corret==0:
    print(str(word) +' is not a palindrome.')
else:
    print(str(word) +' is a palindrome.')
        