#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''
@File : run.py.py
@Time : 2020/6/19
@Author : hackhub 
@Version : 0.0.1
@Contact : hackhub.me@gmail.com
@License : (C)Copyright 2020, HACKHUB-ME
@Desc : None
'''

from scrapy import cmdline
if __name__ == "__main__":
    # cmdline.execute("scrapy crawl skin".split())
    cmdline.execute("scrapy crawl skin --nolog".split())

