#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
第1回演習問題
"""
import numpy as np

########## 課題1(a)
print("Hello World")

########## 課題1(b)i
A = np.array([[1,2,3,4,5],[6,7,8,9,10],[11,12,13,14,15],[16,17,18,19,20]], dtype = float)
b = np.array([1,0,1,0,1],dtype = float)
print("A = ", A) # 表示方法の例
print("b = ", b)

########## 課題1(b)ii
Ab = np.dot(A,b)
print("Ab = ",Ab)
########## 課題1(b)iii

A0 = np.sum(A, axis = 0)
A1 = np.sum(A, axis = 1)

print(A0)
print(A1)
########## 課題1(c) 例
print("--- Kadai 1(c) example ---")
x = 0
for n in range(1, 11): # この指定でnは1から10まで動く
    x = 2*x + 1
    #print("a(", n, ") =", x)
    print(f"a({n}) = {x}")
    
########## 課題1(c)
print("---Kadai 1(c)---")
x = 6
for n in range(1,11):
    if  x % 2 == 0:
        x = x / 2
    else:
        x = 3*x + 1
    print("a(", n, ") = ",x)