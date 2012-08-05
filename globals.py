#! /usr/bin/env python
#coding=utf-8

aa='ccc'

from sgmllib import SGMLParser

class TestC:
    b = 'bb'
    
    def f(self,x):
        print len(globals())

def fun(param):
    x = 0
    print len(globals())
    
fun('cc')

t = TestC()
t.f('g')
