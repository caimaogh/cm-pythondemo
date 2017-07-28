#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# 给定4个数字，要求打印出所有不重复的排列组合
# 3重for循环嵌套加上三个数字互不相等
for i in range(1, 5):
    for j in range(1, 5):
        for k in range(1, 5):
            if(i != j) and (i != k) and (j != k):
                print(i, j, k)

# 输出99乘法表
for a in range(1, 10):
    for b in range(1, 10):
        result = a * b
        print('%d * %d = %3d' % (a, b, result))

# 设有整数i，i+100是一个完全平方数，再加168又是一个完全平方数，求出该整数的值。
import math
for i in range(10000000):
    x = int(math.sqrt(i + 100))
    y = int(math.sqrt(i + 268))
    if(x * x == i + 100) and (y * y == i + 268):
        print(i)
