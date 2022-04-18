import serial
import time
import logging
from resources import base
from datetime import datetime
from resources import data
import sys
import re
import os


def writeToFileRunStatus(filename,Content):
    with open(os.getcwd()+'/'+'Devicelogs'+'/'+filename+'.txt','a') as runstatus:
        runstatus.write(Content)

        
def start_session():
    serial_port=serial.Serial(port=data.portnumber, baudrate=115200, bytesize=8, timeout=2, stopbits=serial.STOPBITS_ONE)
    return serial_port
	
port=start_session()


def write_serialport(command):
    time.sleep(5)
    port.write('\r\n'.encode('utf-8'))
    port.write('\r\n'.encode('utf-8'))
    port.write('\r\n'.encode('utf-8'))
    port.write(command.encode('utf-8'))
    #logger.info("####"+command+"####")
    print("Command executed - "+" "+command)


def SetFacDefault():
    if port.isOpen():
	    port.close()
    port.open()
    write_serialport('SetFacDefault\r\n')
    time.sleep(2)
    start_time = time.time()
    seconds = 10
    while time.time() < start_time+seconds:
        read_port=port.readline()
        if read_port.__len__()<0:
            continue
        try:
            read_data=read_port.decode('unicode_escape')
            '''if ' sysrq: SysRq : Emergency Remount R/O' in read_data:
                print("Factory rested Started")
            if 'tdm playback stop' in read_data:
                print("Factory Reset Completed")
                exit()'''
            print(read_data)
            #writeToFileRunStatus(name,read_data)
        except:
            pass
                
            
def captureLogs(name):
    if port.isOpen():
	    port.close()
    port.open()
    write_serialport('logcat &\r\n')
    time.sleep(2)
    start_time = time.time()
    seconds = 30
    while time.time() < start_time+seconds:
        read_port=port.readline()
        if read_port.__len__()<0:
            continue
        try:
            read_data=read_port.decode('unicode_escape')
            #if 'EAPOL: disable timer tick' in read_data:
                #close_session()
            print(read_data)
            writeToFileRunStatus(name,read_data)
            
        except:
            pass
    

                
def close_session():
    if port.isOpen():
        port.close()
        
