#!/usr/bin/python

import sys

def main():
    arr = [int(x) for x in sys.stdin.readline().split()]
    n = len(arr)
    lis = [1]*n
    for i in xrange(1, n):
        for j in xrange(i):
            if arr[i] > arr[j]:
                lis[i] = max(lis[i], lis[j]+1)
    return max(lis)

if __name__ == '__main__':
    maxv = main()
    print maxv
