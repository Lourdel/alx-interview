#!/usr/bin/python3

"""Module that solves the lockbox challenge"""


def canUnlockAll(boxes):
    """Method to check if boxes are unlocked"""
    n = len(boxes)
    opened = set()
    stack = [0]

    while stack:
        box = stack.pop()
        opened.add(box)
        keys = boxes[box]
        for key in keys:
            if key not in opened and key < n:
                stack.append(key)
    return len(opened) == n
