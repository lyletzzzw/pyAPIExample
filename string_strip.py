#! /usr/bin/env python
#coding=utf-8

formateStr = 'old->%s\t%s\tnew->%s\t%s'
testStr1 = ' abcd '
testStr2 = ' abcd'
testStr3 = 'abcd '

testStr4 = 'AAabcdAA'
testStr5 = 'Aabcd'
testStr6 = 'abcdA'

testStr7 = 'abcd\n'

testStr8 = 'yuiosdfs'

def showStr(testStr,replace=None):
    print formateStr % (testStr,str(len(testStr)),testStr.strip(replace),str(len(testStr.strip(replace))))

showStr(testStr1)
showStr(testStr2)
showStr(testStr3)

showStr(testStr4,'A')
showStr(testStr5,'A')
showStr(testStr6,'A')

showStr(testStr7)

showStr(testStr8,'uy')
