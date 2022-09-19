#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
@created: 28.11.20
@author: felix
"""
import time

from include_rust import is_type_of


def main():
    test_list = list(range(10_000_000))
    test_list.append("failure")

    start = time.perf_counter()
    is_type_of(test_list, list[int])
    print(f"Time needed = {time.perf_counter() - start}")


if __name__ == '__main__':
    main()
