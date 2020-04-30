#!/usr/bin/python3
import time
import os

#Esta funcion verifica el estado del servicio mysql: 0 OK; otro_numero Error
def status():
        max_time = 60
        start_time = time.time()
        status = os.system('systemctl is-active --quiet mysql')
        while status != 0:
                time.sleep(30)
                status = os.system('systemctl is-active --quiet mysql')
                end_time = time.time()
                if end_time - start_time > max_time :
                        return False
        else:
            return True
