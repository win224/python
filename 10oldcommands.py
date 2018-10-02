#!/usr/bin/evn python

import os

from collections import Counter
c = Counter()
with open(os.path.expanduser('~/.bash_history')) as f:
    for line in f:
        cmd = line.strip().split()
        if cmd:
            c[cmd[0]]+=1
            c.most_common(10)