#!/usr/bin/env python
# -*- coding: UTF-8 -*-

from __future__ import unicode_literals
import os
import socket
from datetime import datetime

import jinja2
import yagmail
import psutil

EMAIL_USER = 'royjin@163.com'
EMAIL_PASSWORD = ''
RECIPIENTS = ['royjin@msn.com']

def render(tpl_path, **kwargs):
    path,filename = os.path.split(tpl_path)
    return  jinja2.Environment(loader=jinja2.FileSystemLoader(path or './')
                               ).get_template(filename).render(**kwargs)

def bytes2human(n):
    symbols = ('K', 'M', 'G', 'T', 'P', 'E', 'Z', 'Y')
    prefix = {}