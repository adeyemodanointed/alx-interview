#!/usr/bin/python3
"""N queens Algorithm"""
import sys


def is_valid_state(state, n):
    """Checks for valid states"""
    # check if it is a valid solution
    return len(state) == n


def get_candidates(state, n):
    """Get's candidates fit"""
    if not state:
        return range(n)

    # find the next position in the state to populate
    position = len(state)
    candidates = set(range(n))

    # prune down candidates that place the queen into attacks
    for row, col in enumerate(state):
        # discard column index if occupied
        candidates.discard(col)
        dist = position - row
        # discard diagonals
        candidates.discard(col + dist)
        candidates.discard(col - dist)
    return candidates


def search(state, solutions, n):
    """Used to perform a search"""
    if is_valid_state(state, n):
        solutions.append(state.copy())
        # return

    for candidate in get_candidates(state, n):
        state.append(candidate)
        search(state, solutions, n)
        state.pop()


def solve():
    """Solves the N queen problem"""
    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        sys.exit(1)
    try:
        n = int(sys.argv[1])
    except Exception:
        print("N must be a number")
        sys.exit(1)
    if n < 4:
        print("N must be at least 4")
        sys.exit(1)

    solutions = []
    state = []
    search(state, solutions, n)
    return solutions


if __name__ == "__main__":
    for val in solve():
        sub = []
        for i in val:
            sub.append([i, val[i]])
        print(sub)
