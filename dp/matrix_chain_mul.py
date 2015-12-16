#!/usr/bin/python

import sys

def computecost(p, n):
    m = [[0]*(n) for x in xrange(n)]

    for L in range(2, n):
        for i in range(1, n-L+1):
            j = i+L-1
            m[i][j] = sys.maxint
            for k in xrange(i, j):
                q = m[i][k] + m[k+1][j] + p[i-1]*p[k]*p[j]
                m[i][j] = min(q, m[i][j])
    return m[1][n-1]

def main():
    p = [int(x) for x in sys.stdin.readline().split()]
    return computecost(p, len(p))

if __name__ == '__main__':
    ans = main()
    print ans
