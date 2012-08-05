#! /usr/bin/env python
#coding=utf-8

import os

pathStr = 'c:/'

print [os.path.normcase(el) for el in os.listdir(pathStr)]

print os.path.normcase('C:\\Windows\\Boot\\')
print os.path.normcase('C:/Windows/Boot/')
