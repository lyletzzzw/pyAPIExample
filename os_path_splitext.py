#! /usr/bin/env python
#coding=utf-8

import os
import UserDict

pathStr = 'c:/'

'''
fList = [os.path.normcase(f) for f in os.listdir(pathStr)]
print fList
fList = [os.path.join(pathStr,f) for f in fList]
print fList
fList = [os.path.splitext(f) for f in fList]
print fList
'''

print os.path.splitext('C:/asasdfsaf.txt')

#print UserDict.__module__

print os.path.splitext('asasdfsaf.txt')