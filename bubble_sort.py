#!/usr/bin/env python3
# -*- coding: utf-8 -*-

'''
1. 比较相邻的元素。如果第一个比第二个大，就交换他们两个。
2. 对第0个到第n-1个数据做同样的工作。这时，最大的数就“浮”到了数组最后的位置上。
3. 针对所有的元素重复以上的步骤，除了最后一个。
4. 持续每次对越来越少的元素重复上面的步骤，直到没有任何一对数字需要比较。
'''

def bubble_sort(list):
    for i in range(len(list)):
        for  j in range(1, len(list)-i):
            if list[j-1] > list[j]:
                list[j-1], list[j] = list[j], list[j-1]
    return list

list=[3, 5, 1, 9]
print(bubble_sort(list))