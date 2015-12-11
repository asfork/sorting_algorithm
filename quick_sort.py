#!/usr/bin/env python3
# -*- coding: UTF-8 -*-

'''
1. 从数列中挑出一个元素作为基准数。
2. 分区过程，将比基准数大的放到右边，小于或等于它的数都放到左边。
3. 再对左右区间递归执行第二步，直至各区间只有一个数。
'''

def quick_sort(list):
    return qsort(list, 0, len(list) - 1)

def qsort(list, left, right):
    if left >= right:
        return list
    key = list[left]
    low = left
    high = right
    while low < high:
        while list[high] >= key and low < high:
            high -= 1
        while list[low] <= key and low < high:
            low += 1
        list[low], list[high] = list[high], list[low]
    list[left], list[low] = list[low], list[left]
    qsort(list, left, low-1)
    qsort(list, high+1, right)
    return list

list=[3,5,4,7,6,9,1,10]
print(quick_sort(list))