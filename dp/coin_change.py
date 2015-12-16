#!/usr/bin/python

import sys

def main():
    n = int(sys.stdin.readline())
    s = [ int(x) for x in sys.stdin.readline().split() ]
    s.sort()
    table = [0]*(n+1)
    table[0] = 1
    for i in xrange(len(s)):
        for j in range(s[i], n+1):
            table[j] += table[j-s[i]]
    print table[n]
if __name__ == '__main__':
    main()
