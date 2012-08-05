#! /usr/bin/env python
#coding=utf-8

import string

str="a <nd abc nd > "
print string.replace(str,'nd','+')
print string.replace(str,'nd','+',0)
print string.replace(str,'nd','+',1)
print string.replace(str,'nd','+',2)



