#!/usr/bin/python

import sys

def feb(n, ans):
    if n == 0 or n == 1:
        ans[n] = n
    if ans[n] is None:
        ans[n] = feb(n-1, ans) + feb(n-2, ans)
    return ans[n]
    
def main():
    n = int(sys.stdin.readline())
    ans = [None]*(n+1)
    return feb(n, ans)

if __name__ == '__main__':
    ans = main()
    print ans
