#!/usr/bin/python

import sys

def knapsack(w, wt, val, n):
    knaps = [[0]*(n+1) for j in xrange(n+1)]

    for i in xrange(1, n+1):
        if wt[i-1] > w:
            knaps[i] = knaps[i-1]
        else:

        for j in xrange(1, i)

def main():
    w = int(sys.stdin.readline())
    wt = [int(x) for x in sys.stdin.readline().split()]
    val = [int(x) for x in sys.stdin.readline().split()]
    return knapsack(w, wt, val, len(n))

if __name__ == '__main__':
    main()

