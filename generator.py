#!/usr/bin/env python3
# -*- coding: utf-8 -*-

g = (x * x for x in range(10))
print(next(g))
print(next(g))
for n in g:
    print(n)