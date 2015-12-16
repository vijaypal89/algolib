#!/usr/bin/python

import sys

def main():
    arr = [int(x) for x in sys.stdin.readline().split()]
    arr.sort()
    i=0; j=1; n = len(arr)
    count = 0
    for i in range(n-2):
        k = i + 2
        for j in range(i+1, n-1):
            while k < n and arr[i]+arr[j]>arr[k]:
                k += 1
            count += (k-j-1)
    print count

if __name__ == '__main__':
    main()
