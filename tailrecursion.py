#!/usr/bin/env python3
# -*- coding: utf-8 -*-

'''
Python 默认编译器没有对尾递归做优化，超过 1000 仍旧会报错
'''

def fact(n):
    return fact_iter(n, 1)

def fact_iter(count, i):
    if count == 1:
        return i
    else:
        return fact_iter(count - 1, count * i)

print(fact(1000))