import serial
import time
import logging
from resources import base
from datetime import datetime
from resources import data
import sys
import re
'''tm=datetime.now().strftime("%m-%d-%Y %H%M%S")
logging.basicConfig(filename=base.create_file("logs" ,"Device_OTA_logs"+tm+".log"),
                    format='%(asctime)s %(message)s',
                    filemode='a')
logger=logging.getLogger()
  
    #Setting the threshold of logger to DEBUG
logger.setLevel(logging.INFO)'''

def getLogger(name):
    # logger.getLogger returns the cached logger when called multiple times
    # logger.Logger created a new one every time and that avoids adding
    # duplicate handlers 
    logger = logging.Logger(name)
    logger.setLevel(logging.DEBUG)
    handler = logging.FileHandler(os.path.join('./logs/Devicelogs/', name + tm+ '.log'), 'a')
    logger.addHandler(handler)
    return logger
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

def deviceReboot():
    if port.isOpen():
	    port.close()
    port.open()
    write_serialport('reboot\r\n')
    time.sleep(2)
    while True:
        read_port=port.readline()
        if read_port.__len__()<0:
            continue
        try:
            read_data=read_port.decode('unicode_escape')
            if ' sysrq: SysRq : Emergency Remount R/O' in read_data:
                print("Factory rested Started")
            if 'tdm playback stop' in read_data:
                print("Device reboot Completed")
                return True
            print(read_data)
            
            #logger.info("#"+read_data+"#")            
        except:
            return False

def SetFacDefault():
    if port.isOpen():
	    port.close()
    port.open()
    write_serialport('SetFacDefault\r\n')
    time.sleep(2)
    while True:
        read_port=port.readline()
        if read_port.__len__()<0:
            continue
        try:
            read_data=read_port.decode('unicode_escape')
            if ' sysrq: SysRq : Emergency Remount R/O' in read_data:
                print("Factory rested Started")
            if 'tdm playback stop' in read_data:
                print("Factory Reset Completed")
                return True
            print(read_data)
            #logger.info("#"+read_data+"#")            
        except:
            return False


def captureLogs(name):
    if port.isOpen():
	    port.close()
    port.open()
    #write_serialport('logcat -c\r\n')
    write_serialport('logcat &\r\n')
    time.sleep(2)
    while True:
        read_port=port.readline()
        if read_port.__len__()<0:
            continue
        try:
            read_data=read_port.decode('unicode_escape')
            if 'EAPOL: disable timer tick' in read_data:
                break
            print(read_data)
            log=getLogger(name)
            log.info(read_data)          
        except:
            return False
            
def connect_to_wifi():
    write_serialport('LUCI_local 125 TP-Link_7632,marvel@1920\r\n')
    write_serialport('logcat &\r\n')
    write_serialport('netcfg\r\n')
    time.sleep(2)
    while True:
        data1=port.readline()
        if data1.__len__()<0:
            continue
        data1 = data1.decode('unicode_escape')
        print(data1)
        if 'wlan0'  in  data1:
            print(data1)
            datalist=re.split(r'[\n\t\f\v\r ]+', data1)
            print(datalist[2])
            ip_add=datalist[2]
            if ip_add.startswith('172') or ip_add.startswith('192'):
               print("connected to WIFI succsessfully")
        print(data1)

def ipcheck():
    if port.isOpen():
        port.close()
    port.open()
    print("netcfg")
    time.sleep(5)
    write_serialport('netcfg \r\n')
    time.sleep(2)
    
    while True:
        data1=port.readline()
        if data1.__len__()<0:
            continue
        data1 = data1.decode('unicode_escape')
        print(data1)
        
        if 'wlan0'  in  data1:
            print(data1)
            datalist=re.split(r'[\n\t\f\v\r ]+', data1)
            print(datalist[2])
            ip_add=datalist[2]
            if ip_add.startswith('172') or ip_add.startswith('192'):
                deviceReboot()
                time.sleep(4)
                LS10_OTA_verification()   
            else:
                #SetFacDefault()
                #os.system("python3 GoogleHomeApp.py")
                time.sleep(10)
                deviceReboot()
                time.sleep(10)
                write_serialport('LUCI_local 125 TP-Link_7632,marvel@1920\r\n')
                time.sleep(40)
                ipcheck()
                #LS10_OTA_verification()
                
def close_session():
    if port.isOpen():
        port.close()
        
