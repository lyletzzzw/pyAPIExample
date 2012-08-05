#! /usr/bin/env python
#coding=utf-8

import string

str="a <nd abc <nd nd > "

print string.split(str)
print string.split(str,'a')
print string.split(str,' ',1)
print string.split(str,' ',2)
print string.split(str,'sdf')


