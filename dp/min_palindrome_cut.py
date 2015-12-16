#!/usr/bin/python

import sys

def minPalindromeCut(s, n):
    c = [0 for i in xrange(n)]
    p = [[False]*n for x in xrange(n)]
    #1char str in palindrome
    for i in xrange(n):
        p[i][i] = True
    for l in xrange(2, n+1):
        for i in xrange(n-l+1):
            j = l+i-1
            if l == 2:
                if s[i] == s[j]:
                    p[i][j] = True
            else:
                if s[i] == s[j] and p[i+1][j-1]:
                    p[i][j] = True
    for i in xrange(n):
        if p[0][i]:
            c[i] = 0
        else:
            c[i] = sys.maxint
            for j in xrange(i):
                if p[j+1][i]:
                    c[i] = min(c[i], 1+c[j])
    return c[n-1]

def main():
    s = sys.stdin.readline().strip()
    mincut = minPalindromeCut(s, len(s))
    return mincut

if __name__ == '__main__':
    ans = main()
    print ans
