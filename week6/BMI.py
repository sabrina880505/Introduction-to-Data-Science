# -*- coding: utf-8 -*-
"""Untitled0.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/12l-QTSF_ftwCzMBXgcdgZBEoe-5bd7Cn
"""

#判斷 BMI 的類別標籤
height=int(input('請輸入您的身高(公分):'))
weight=int(input('請輸入您的體重(公斤):'))
bmi=weight/(height/100)**2

if bmi <18.5:
  print("身高{}公分、體重{}公斤、是Under weight".format(height,weight))
elif 18.5<= bmi <25:
  print("身高{}公分、體重{}公斤、是Normal weight".format(height,weight))
elif 25<= bmi <30:
  print("身高{}公分、體重{}公斤、是Over weight".format(height,weight))
else:
  print("身高{}公分、體重{}公斤、是Obese".format(height,weight))

