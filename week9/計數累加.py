# -*- coding: utf-8 -*-
"""Untitled

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1zYNMbBfyXXR9A0B5yf9E8My-PVZxDOb-
"""

x = int(input("請輸入起始的整數:"))
y = int(input("請輸入終止的整數:"))
odd_summation = 0 
i = x 
while i <= y: 
    
    if i % 2 == 1:
        odd_summation = odd_summation + i 
    i += 1 
print("======")
print(odd_summation)

