#!/usr/bin/python

import sys

def main():
    n, k = [int(x) for x in sys.stdin.readline().split()]
    eggFloor = [[0]*(k+1) for x in xrange(n+1)]
    #for 0 floor tries 0, 1 floor 1 tries
    for i in xrange(1, n+1):
        eggFloor[i][0] = 0
        eggFloor[i][1] = 1
    #for 1 egg , tries will be j
    for j in xrange(1, k+1):
        eggFloor[1][j] = j
    #for rest of floor and eggs
    for i in xrange(2, n+1):
        for j in xrange(2, k+1):
            eggFloor[i][j] = sys.maxint
            for x in xrange(1, j+1):
                res = 1 + max(eggFloor[i-1][x-1], eggFloor[i][j-x])
                eggFloor[i][j] = min(res, eggFloor[i][j])
    return eggFloor[n][k]

if __name__ == '__main__':
    ans = main()
    print ans
