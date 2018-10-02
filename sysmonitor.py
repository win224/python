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
    for i,s in enumerate(symbols):
        prefix[s] = 1 << (i+1) * 10
    for s in reversed(symbols):
        if n >= prefix[s]:
            value = float(n) / prefix[s]
            return  '%.1f%s' %(value,s)
    return  "%sB" % n

def get_cpu_info():
    cpu_count = psutil.cpu.count()
    cpu_percent = psutil.cpu.percent(interval=1)
    return dict(cpu_count=cpu_count,cpu_percent=cpu_percent)

def get_momory_info():
    virtual_mem = psutil.virtual_memory()

    mem_total = bytes2human(virtual_mem.total)
    mem_percent = virtual_mem.percent
    mem_free = bytes2human(virtual_mem.free + virtual_mem.buffers + virtual_mem.cached)
    mem_used = bytes2human(virtual_mem.total * virtual_mem.percent)

    return dict(mem_total=mem_total,mem_percent=mem_percent,mem_free=mem_free,mem_used=mem_used)

def get_disk_info():
    disk_usage = psutil.disk_usage('/')

    disk_total = bytes2human(disk_usage.total)
    disk_percent = disk_usage.percent
    disk_free = bytes2human(disk_usage.free)
    disk_used = bytes2human(disk_usage.used)

    return  dict(disk_total=disk_total,disk_percent=disk_percent,disk_free=disk_free,disk_used=disk_used)

def get_boot_info():
    boot_time = datetime.fromtimestamp(psutil.boot_time()).strftime("%Y-%m-%d %H:%M:%S")
    #boot_time = datetime.fromtimestamp(psutil.boot_time()).strftime("%Y-%m-%d %H:%M:%S")
    return dict(boot_time=boot_time)

def collect_monitor_data():
    data = {}
    data.update(get_boot_info())
    data.update(get_cpu_info())
    data_update(get_momory_info())
    data.update(get_disk_info())
    return data


def main():
    hostname = socket.gethostname()
    data = collect_monitor_data()
    data.update(dict(hostname=hostname))

    content = render('monitor.html',**data)
    print content

    with yagmail.SMTP(user=EMAIL_USER,password=EMAIL_PASSWORD,host='smtp.163.com', port=25) as yag:
        for recipient in RECIPIENTS:
            yag.send(recipient,"监控信息".encode('utf_8'), content.encode('uft-8'))

if __name__ == '__main__':
    main()


#https://github.com/Toskajin/python_for_linux_system_administration/blob/master/chapter6/section3/monitor.py