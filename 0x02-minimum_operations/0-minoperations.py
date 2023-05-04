#!/usr/bin/python3
"""Module defines function to determine the minimum number of operations"""

import math


def minOperations(n):
    """
    Method determines the minimum number of operations needed to result in
    exactly nH characters in the file.
    it returns an integer and 0 if n is impossible
    """

    if n == 1:
        return 0
    
    primes = get_primes(int(math.sqrt(n)))
    
    op_list = [float('inf')] * (n+1)
    op_list[1] = 0
    
    for i in range(2, n+1):
        for j in primes:
            if i % j == 0:
                op_list[i] = min(op_list[i], op_list[j] + i//j)
        
        if op_list[i] == float('inf'):
            op_list[i] = i
    
    return op_list[n] if op_list[n] != float('inf') else 0

def get_primes(n):
    """Method to get prime factors of n"""
    primes = []
    selection = [True] * (n+1)
    for i in range(2, int(math.sqrt(n))+1):
        if selection[i]:
            for j in range(i*i, n+1, i):
                selection[j] = False
    for i in range(2, n+1):
        if selection[i]:
            primes.append(i)
    return primes

