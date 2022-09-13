#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
sort algorithm example
from https://cs50.jp/x/2021/week3/notes/
"""
from typing import Callable


def gen_list() -> list[int]:
    return [6, 3, 8, 5, 2, 7, 4, 1]


def selection_sort(a: list[int]) -> list[int]:
    if len(a) <= 1:
        return a
    for i in range(0, len(a)):
        min_idx = i
        for j in range(i, len(a)):
            if a[j] < a[min_idx]:
                min_idx = j
        if min_idx != i:
            a[min_idx], a[i] = a[i], a[min_idx]
    return a


def bubble_sort(a: list[int]) -> list[int]:
    if len(a) <= 1:
        return a
    for i in range(0, len(a) - 1):
        for j in range(1, len(a) - i):
            if a[j] < a[j - 1]:
                a[j], a[j - 1] = a[j - 1], a[j]
    return a


def merge_sort(a: list[int]) -> list[int]:
    if len(a) <= 1:
        return a
    t = int(len(a) / 2)
    l = merge_sort(a[:t])
    r = merge_sort(a[t:])
    a = list()

    while True:
        if len(l) == 0 and len(r) > 0:
            a.extend(r)
            break
        elif len(l) > 0 and len(r) == 0:
            a.extend(l)
            break
        if l[0] < r[0]:
            a.append(l.pop(0))
        else:
            a.append(r.pop(0))
    return a


def run_a_sort(name: str, f: Callable):
    print(name)
    a = gen_list()
    print(a)
    a = f(a)
    print(a)


def main():
    """main"""
    run_a_sort("selection sort", selection_sort)
    run_a_sort("bubble sort", bubble_sort)
    run_a_sort("merge sort", merge_sort)


if __name__ == "__main__":
    main()
