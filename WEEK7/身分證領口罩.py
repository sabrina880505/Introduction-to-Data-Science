# -*- coding: utf-8 -*-
"""Untitled0.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1uxsJdIQlnOKCn2mSX8rh9ehT_UPFHVOw
"""

#依身分證字號尾數決定星期幾可以購買口罩
id=int(input('請輸入您身分證字號的尾數：'))
if id%2 ==0:
  print('星期二四六日領')
else :
  print('星期一三五日領')

