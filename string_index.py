#! /usr/bin/env python
#coding=utf-8

import string

line1="and < abc >"
line2="a b > c"

print string.index(line1,'nd',0,3)
print string.index(line2,'a b')
try:
    print string.index(line2,'d')
except ValueError:
    print u"未找到子字符串！！！"

