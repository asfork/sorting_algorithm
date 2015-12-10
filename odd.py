#!/usr/bin/env python3
# -*- coding: utf-8 -*-

L = []
n = 1
while n <= 99:
    L.append(n)
    n = n + 2

print(L[2:5])
print(L[-5:-2])
print(L[:10:2])