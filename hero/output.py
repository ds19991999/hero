#!/usr/bin/env python
# -*- coding:utf-8 -*-
'''
@File : color.py
@Time : 2020/06/17 09:35:46
@Author : hackhub 
@Version : 0.0.1
@Contact : hackhub.me@gmail.com
@License : (C)Copyright 2020, HACKHUB-ME
@Desc : None
'''

from rich import print
import time

def plus_print(str, level=0):
    str_head = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
    level_str = "<output>"
    color = "green"
    if level == 1:
        level_str = "<Warn>"
        color = "yellow"
    elif level >=2:
        level_str = "<Error>"
        color = "red"     
    str_out = "[bold {}]{} {}[/bold {}] [bold white]{}[/bold white]".format(color, str_head, level_str, color, str)
    str_log = "{} {} {}".format(str_head, level_str, str)
    if level_str=="<Warn>" or level_str=="<Error>":
        write_log(str_log)
    print(str_out)

def write_log(str_log):
    str_head = time.strftime("%Y-%m-%d", time.localtime())
    log_file = str_head+".log"
    with open(log_file, "a", encoding="utf-8") as log_file:
        log_file.write(str_log+"\n")

