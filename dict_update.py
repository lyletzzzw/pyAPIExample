#! /usr/bin/env python
#coding=utf-8

dict={'name':'lyle','id':'l'}
print type(dict)
print dict
dict.update(name=1)
print dict
a = (('a','b'),('1','2'))#注意这里必须是2个以上
dict.update(a)
print a
dict.update({'title':'title1','id':'2'})
print dict
