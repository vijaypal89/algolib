#!/usr/bin/python

import sys

def find_max_sum(arr, n):
    msis = [i for i in arr]
    for i in xrange(1, n):
        for j in xrange(i):
            if arr[i] > arr[j] and msis[i] < msis[j] + arr[i]:
                msis[i] = msis[j] + arr[i]
    return max(msis)

def main():
    arr = [int(x) for x in sys.stdin.readline().split()]
    res = find_max_sum(arr, len(arr))
    return res

if __name__ == '__main__':
    ans = main()
    print ans
