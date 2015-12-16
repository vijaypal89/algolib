#!/usr/bin/python

import sys

def sel_n_k(n, k):
    c = [[0]*(k+1) for j in xrange(n+1)]
    for i in xrange(1, k+1):
        c[i][i] = 1
    for i in xrange(1, n+1):
        c[i][0] = 1
    for i in xrange(1, n+1):
        for j in xrange(1, min(i, k+1)):
            c[i][j] = c[i-1][j-1] + c[i-1][j]
    return c[n][k]

def main():
    #C(n, k) = C(n-1, k-1) + C(n-1, k)
    #C(n, 0) = C(n, n) = 1
    n, k = [int(x) for x in sys.stdin.readline().split()]
    return sel_n_k(n, k)

if __name__ == '__main__':
    ans = main()
    print ans
