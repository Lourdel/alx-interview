#!/usr/bin/python3
"""Module defines function to determine the minimum number of operations"""


def operations_nu(number):
    """calculates the minimum number of operations"""
    cnt = 1
    op_list = []
    val = number
    while val != 1:
        cnt += 1
        if val % cnt == 0:
            while (val % cnt == 0 and val != 1):
                val /= cnt
                op_list.append(cnt)

    return op_list


def minOperations(n):
    """Method Returns sum of operations until n H """
    if n < 2 or type(n) is not int:
        return 0
    values = operations_nu(n)
    return sum(values)
