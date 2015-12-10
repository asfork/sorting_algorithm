#!/usr/bin/env python3
# -*- coding: utf-8 -*-

' Tower of Hanoi '

def move(n, a, b, c):
    if n == 0:
        return
    move(n - 1, a, c, b)
    print(a, '-->', c)
    move(n - 1, b, a, c)

print(move(4, 'A', 'B', 'C'))