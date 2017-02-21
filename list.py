#!/usr/bin/python

import os
import sys

path = str(sys.argv[1])
dir = open('dirs', 'r')
for dir in dir.readlines():
        dir = dir.replace("\n","")
        path2 = path + dir
        tmp = os.path.isdir(path2)
        if tmp:
                print "\033[1;35m" + path2 + "\033[1;32m"

files = open('files', 'r')
for file in files:
        file = file.replace("\n","")
        path2 = path + file
        tmp = os.path.isfile(path2)
        if tmp:
                print "\033[1;33m" + path2 + "\033[1;32m"