#! /usr/bin/env python
#coding=utf-8

import os

pathStr = 'c:/'

fList = [os.path.normcase(el) for el in os.listdir(pathStr)]
fList = [os.path.join(pathStr,f) for f in fList]

print fList

