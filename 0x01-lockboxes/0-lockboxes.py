#!/usr/bin/python3
"""Module that solves the lockbox challenge"""


def canUnlockAll(boxes):
    """Method to check if boxes are unlocked"""
    n = len(boxes)
    opened = [False] * n
    opened[0] = True

    stack = [0]

    while stack:
        box = stack.pop()
        for key in boxes[box]:
            if key < n and not opened[key]:
                opened[key] = True
                stack.append(key)

    return all(opened)
