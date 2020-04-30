#!/usr/bin/python3
import time
import os

def status():
        status = os.system('systemctl is-active --quiet mysql')
        while status != 0:
                time.sleep(30)
                status = os.system('systemctl is-active --quiet mysql')
        else:
            return True
