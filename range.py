#!/usr/bin/env python3
# -*- coding: utf-8 -*-

L = []
for x in range(1, 11):
    L.append(x * x)

print(L)
print([x * x for x in range(1, 11)])
print([x * x for x in range(1, 11) if x % 2 == 0])
print([m + n for m in 'ABC' for n in 'XYZ'])

d = {'x': 'A', 'y': 'B', 'z': 'C'}
print([m + '=' + n for m, n in d.items()])