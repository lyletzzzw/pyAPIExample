#! /usr/bin/env python
#coding=utf-8

import re

email = "tony@tiremove_thisger.net"
matchObj = re.search('remove_this',email)
print matchObj

matchObj1 = re.search('remove_THIS',email)
matchObj2 = re.search('remove_THIS',email,flags=re.IGNORECASE)

print matchObj1
print matchObj2
