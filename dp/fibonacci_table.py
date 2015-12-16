#!/usr/bin/python

import sys

def main():
    n = int(sys.stdin.readline())
    if not n:
        return 0
    elif n == 1:
        return 1
    ans = [0 for i in range(n+1) ]
    ans[1] = 1
    for i in range(2, n+1):
        ans[i] = ans[i-1] + ans[i-2]
    return ans[n]

if __name__ == '__main__':
    ans = main()
    print ans
