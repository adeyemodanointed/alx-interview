#!/usr/bin/python3
"""Lock boxes module"""


def canUnlockAll(boxes):
    """Check if all boxes to unlock all"""
    n = len(boxes)
    s_boxes = set([0])
    u_boxes = set(boxes[0]).difference(set([0]))
    while len(u_boxes) > 0:
        box_idx = u_boxes.pop()
        if not box_idx or box_idx >= n or box_idx < 0:
            continue
        if box_idx not in s_boxes:
            u_boxes = u_boxes.union(boxes[box_idx])
            s_boxes.add(box_idx)
    return n == len(s_boxes)
