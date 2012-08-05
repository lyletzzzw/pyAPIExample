#! /usr/bin/env python
#coding=utf-8

import string

line1="and < abc >"
line2="a b > c"

print string.find(line1,'nd',0,3)
print string.find(line2,'a b')
print string.find(line2,'d')

