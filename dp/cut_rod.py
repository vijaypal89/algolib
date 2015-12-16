#!/usr/bin/python

import sys

def cutRod(price, n):
    val = [0 for x in xrange(n+1)]
    #val[n] = max(price[i] + val[n-i-1])
    for i in xrange(1, n+1):
        res = -1
        for j in xrange(i):
            res = max(res, price[j] + val[i-j-1])
        val[i] = res
    return val[n]

def main():
    price = [int(x) for x in sys.stdin.readline().split()]
    maxp = cutRod(price, len(price))
    return maxp

if __name__ == '__main__':
    ans = main()
    print ans
