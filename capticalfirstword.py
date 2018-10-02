#!/usr/bin/env python
from __future__ import print_function
with open('data.txt') as inf, open('out.txt','w') as outf:
    for line in inf:
        print(*[word.capitalize() for word in line.split()],file=outf)


with open('data.txt') as inf, open('out.txt','w')as outf
    for line in inf:
        outf.write("".join([word.capitalize() for word in line.split()]))
        outf.write("\n")