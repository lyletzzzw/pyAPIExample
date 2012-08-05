#! /usr/bin/env python
#coding=utf-8

list1=['a','b','c']
list2=['h','j']
print list1

list1.extend(list2)
print list1

list2=[1,'2']
list1.extend(list2)
print list1

list1.extend(1)
print list1