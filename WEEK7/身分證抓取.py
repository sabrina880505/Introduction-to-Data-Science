# -*- coding: utf-8 -*-
"""Untitled0.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1uxsJdIQlnOKCn2mSX8rh9ehT_UPFHVOw
"""

id_number = input("請輸入身分證字號：")
id_last_digit = id_number[-1]
id_last_digit = int(id_last_digit)
if id_last_digit % 2 == 0:
    ans = "星期二四六日領"
else:
    ans = "星期一三五日領"
print(ans)

