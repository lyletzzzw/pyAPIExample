#! /usr/bin/env python
#coding=utf-8

import re

patternRe = re.compile('^AA')
print(patternRe.search('AAbbb'))

