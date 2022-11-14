#! /usr/bin/env python3

import os
import shutil
import psutil
import socket
import emails

def check_disk_usage(disk):
    """Verifies that there's enough free space on disk"""
    du = shutil.disk_usage(disk)
    free = du.free / du.total * 100
    print(free)
    return free > 20
def check_memory_usage():
    """available memory in linux-instance, in byte"""
    mu = psutil.virtual_memory().available
    total = mu/ (1024.0 ** 2)
    print(total)
    return total > 500
def check_cpu_usage():
    """Verifies that there's enough unused CPU"""
    usage = psutil.cpu_percent(1)
    print(usage)
    return usage < 80
def send_email(subject):
    email = emails.generate_email("jack******@gmail.com", "doll****@gmail.com",
                                 subject,"Please check your system and resolve the issue as soon as possible","")
    print(email)
    emails.send_email(email)
if  not check_cpu_usage():
    subject = "Error - CPU usage is over 80%"
    print(subject)
    send_email(subject)
if not check_memory_usage():
    subject = "Error - Available memory is less than 500MB"
    print(subject)
if not check_disk_usage('/'):
    subject = "Error -Available disk space is less than 20%"
    print(subject)
    send_email(subject)

else:
    pass
