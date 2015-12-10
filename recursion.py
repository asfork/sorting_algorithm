#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Python 中默认调用堆栈长度是 1000 ，超过即报错
def fact(n):
    if n == 1:
        return 1
    return n * fact(n -1)

print(fact(100))