#!/usr/bin/python

import sys

def find_longest_palindrome(s, n):
    L = [[0 for i in xrange(n)] for x in xrange(n)]
    #for all char and 2char substr
    for i in xrange(n):
        L[i][i] = 1
    for i in xrange(2, n+1):
        #maintain j&k such that it computes all palindrome of length i
        for j in xrange(n-i+1):
            k = i+j-1
            if s[j] == s[k] and j+1 == k:
                L[j][k] = 2
            elif s[j] == s[k]:
                L[j][k] = 2+L[j+1][k-1]
            else:
                L[j][k] = max(L[j+1][k], L[j][k-1])
    return L[0][n-1]

def main():
    s = sys.stdin.readline().strip()
    ans = find_longest_palindrome(s, len(s))
    return ans

if __name__ == '__main__':
    ans = main()
    print ans
