# -*- coding: utf-8 -*-
"""week8 A106260082.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1CnpfDm0VMyz8U-tAxp2_Ze18RPTVpNhF
"""

user_int = int(input("請輸入一個正整數:"))
if user_int % 15 == 0:
    print("Fizz Buzz")
elif user_int % 5 == 0:
    print("Buzz")
elif user_int % 3 == 0:
    print("Fizz")
else:
    print(user_int)

