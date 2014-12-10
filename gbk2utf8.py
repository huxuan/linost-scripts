#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
File: gbk2utf8.py
Author: huxuan
Email: i(at)huxuan.org
Description: Convert gbk to utf8.
"""

filename = raw_input('Input the filename for conversion:')
filename_new = 'utf8_{}'.format(filename)
with open(filename) as fin:
    with open(filename_new, 'w') as fout:
        for line in fin:
            print >>fout, line.decode('gbk').encode('utf8'),
