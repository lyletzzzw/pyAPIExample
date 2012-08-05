#! /usr/bin/env python
#coding=utf-8

import urllib

'''
sock = urllib.urlopen('http://diveintopython.org')
html1 = sock.info()
html2 = sock.read()
sock.close()

print html1
print html2
'''


print '--------------------------------------------'
data=urllib.urlencode({'wd':'AAA'})
print data
sock = urllib.urlopen('http://www.baidu.com',data)
html = sock.read()
sock.close()

print html
