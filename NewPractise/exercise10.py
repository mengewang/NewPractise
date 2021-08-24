# -*- coding: utf-8 -*-
"""
Created on Sun Aug 22 14:00:04 2021

@author: lenovo
"""

import random
a=random.sample(range(1,30),12)
b=random.sample(range(1,30), 16)
print([i for i in set(a) if i in b])