# -*- coding: utf-8 -*-
"""Untitled0.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1uxsJdIQlnOKCn2mSX8rh9ehT_UPFHVOw
"""

movie_title = input('請輸入電影的名稱:')
movie_rating = input('請輸入電影的評等:')
movie_rating = float(movie_rating)

if movie_rating > 7:
    print("{}的評分為 {} 分值得去看！".format(movie_title, movie_rating))
if movie_rating <= 7:
    print("{}的評分為 {} 分不值得去看，浪費時間！".format(movie_title, movie_rating))

