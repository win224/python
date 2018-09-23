#!/usr/bin/python

import os
import os.path

filename = '/tmp/test.txt'

if os.path.isfile(filename):
    f1 = open(file,'a+')

while True:
    line = raw_input('Enter sth>')
    if line == 'q' or line == 'quit':
        break

    f1.write(line+'\n')