#!/usr/bin/python

import sys

def main():
    s1 = sys.stdin.readline().strip()
    s2 = sys.stdin.readline().strip()
    m = len(s1)
    n = len(s2)
    ll = [[0]*(n+1) for i in xrange(m+1)]
    for i in xrange(m+1):
        for j in xrange(n+1):
            if i == 0 or j == 0:
                ll[i][j] = 0
            elif s1[i-1] == s2[j-1]:
                ll[i][j] = 1 + ll[i-1][j-1]
            else:
                ll[i][j] = max(ll[i-1][j], ll[i][j-1])
    return ll[m][n]

if __name__ == '__main__':
    ans = main()
    print ans
