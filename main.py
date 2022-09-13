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
    for i in range(0, len(a)):
        min_idx = i
        for j in range(i, len(a)):
            if a[j] < a[min_idx]:
                min_idx = j
        if min_idx != i:
            a[min_idx], a[i] = a[i], a[min_idx]
    return a


def bubble_sort(a: list[int]) -> list[int]:
    for i in range(0, len(a) - 1):
        for j in range(1, len(a) - i):
            if a[j] < a[j - 1]:
                a[j], a[j - 1] = a[j - 1], a[j]
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


if __name__ == "__main__":
    main()
