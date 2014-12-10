#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
File: chinese2pinyin.py
Author: huxuan
Email: i(at)huxuan.org
Description: Convert Chinese to Pinyin.
"""

import pinyin

filename = raw_input('Input the filename for conversion:')
filename_new = 'pinyin_{}'.format(filename)
with open(filename) as fin:
    with open(filename_new, 'w') as fout:
        for line in fin:
            print >>fout, pinyin.get(line.decode('utf8')).encode('utf8'),
