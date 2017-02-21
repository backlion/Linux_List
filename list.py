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
files = open('dirs', 'r')
extensions = open('exts', 'r')
for file in files:
        file = file.replace("\n","")
        path2 = path + file
        tmp = os.path.isfile(path2)
        if tmp:
                print "\033[1;33m" + path2 + "\033[1;32m"
        path3 = path2 + 's'
        tmp = os.path.isfile(path3)
        if tmp:
                print "\033[1;33m" + path3 + "\033[1;32m"
        # check extensions too
        for ext in extensions:
                ext = ext.replace("\n","")
                path4 = path2 + ext
                path5 = path3 + ext
                tmp = os.path.isfile(path4)
                if tmp:
                        print "\033[1;33m" + path4 + "\033[1;32m"
                tmp = os.path.isfile(path5)
                if tmp:
                        print "\033[1;33m" + path5 + "\033[1;32m"