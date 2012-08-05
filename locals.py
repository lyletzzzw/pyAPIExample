#! /usr/bin/env python
#coding=utf-8

aa='ccc'

class TestC:
    b = 'bb'
    
    def f(self,x):
        print locals()

def fun(param):
    x = 0
    print locals()
    
fun('cc')

t = TestC()
t.f('g')
