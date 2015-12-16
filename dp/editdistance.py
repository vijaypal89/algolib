#!/usr/bin/python

import sys

def main():
    s1 = sys.stdin.readline().strip()
    s2 = sys.stdin.readline().strip()
    m = len(s1); n = len(s2)
    dp = [[0]*(n+1) for i in xrange(m+1)]
    for x in xrange(m+1):
        for y in xrange(n+1):
            if x == 0:
                dp[x][y] = y
            elif y == 0:
                dp[x][y] = x
            elif s1[x-1] == s2[y-1]:
                dp[x][y] = dp[x-1][y-1]
            else:
                dp[x][y] = 1 + min(dp[x-1][y-1], dp[x][y-1], dp[x-1][y])
    return dp[m][n]

if __name__ == '__main__':
    ans = main()
    print ans
