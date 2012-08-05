#! /usr/bin/env python
#coding=utf-8

import re

#匹配后处理函数
def dashrepl(matchObj):
    if matchObj.group(0)=='-':
        return ' '
    else:
        return '-'

#r对斜杠\的处理，不进行转移工作
print u'API文档例子：'+re.sub(r'def\s+([a-zA-Z_][a-zA-Z_0-9]*)\s*\(\s*\):',
    r'\1(void)\n{',
    'def myfunc():')

#匹配字符串，替换字符串
print u'repl替换字符串：'+re.sub('-{1,1}','+','pro----gram-files')

#匹配字符串，调用dashrepl处理替换字符串
print u'repl为函数处理替换的字符串：'+re.sub('-{1,2}',dashrepl,'pro----gram-files')


#匹配替换匹配的次数
print u'替换匹配的次数：'+re.sub('-{1,1}','+','pro----gram-files',2)

#忽略匹配字符串的大小写
print u'flags 忽略字符串大小写：'+re.sub(r'\sAND\s',' & ','Baked Beans And Spam',flags=re.IGNORECASE)


print re.sub(r'归属地报表_(\d+)',r'\1','归属地报表_10')

