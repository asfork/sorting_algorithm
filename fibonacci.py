#!/usr/bin/env python3
# -*- coding: utf-8 -*-

' a test module '

__author__ = 'Steve Zhang'

def fib(max):
    n, a, b = 0, 0, 1
    while n < max:
        print(b)
        a, b = b, a + b
        n = n + 1
    return 'done'

print(fib(5))