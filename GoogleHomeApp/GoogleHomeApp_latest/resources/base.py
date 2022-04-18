import os
import subprocess
import platform
from datetime import date
import base64
import socket
import time
from resources import android
from resources import data
from appium import webdriver
from appium.webdriver.appium_service import AppiumService


def working_dri():
    cwd=os.getcwd()
    return cwd
 
def check_port_in_use():
    a_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    location = ("0.0.0.0", 4723)
    result_of_check = a_socket.connect_ex(location)
    return a_socket,result_of_check
    

    
def create_file(dirname,filename):
    today = date.today()
    d4 = today.strftime("%b-%d-%Y")
    mainpath=os.getcwd()+os.sep+dirname+os.sep+ d4
    if not os.path.exists(mainpath):
        os.mkdir(mainpath)
        os.chmod(mainpath, 0o777)
        return os.path.join(mainpath, filename)
    else:
        return os.path.join(mainpath, filename)
 
sp=os.path.sep
DEFAULT_PORT = 4723
#fucntions to Start Appiumt CLI Server
def start_appium_server():
    #appium_service = AppiumService()
    #appium_service.start(args=['--address', '0.0.0.0', '-p', str(DEFAULT_PORT)])
    os.system("start /B start cmd.exe @cmd /k appium -a 127.0.0.1 -p 4723")
    print("Appium server started")

def stop_appium_server():
    #S_obj,flag=check_port_in_use()
    #os_name = platform.system()
    #if os_name == 'Windows':
    #os.system('pkill -9 -f appium')
    os.system("taskkill /F /IM cmd.exe")
    os.system("taskkill /F /IM node.exe")
    #os.system("taskkill /F /IM cmd.exe")
    print('Appium Server stopped successfully')
    #else:
     #   os.system("/usr/bin/killall -KILL node")        

def capabilities():
    "Setup for the test"
    desired_caps = {}
    desired_caps['automationName'] = 'UiAutomator2'
    #desired_caps['browserName '] = 'Chrome'
    desired_caps['platformName'] = 'Android'
    desired_caps['platformVersion'] = android.getAndroidVersion()
    desired_caps['deviceName'] = android.getDeviceName()
    desired_caps['uuid'] = android.getDeviceUUID()
    desired_caps['appPackage'] = data.appPackageName
    desired_caps['appActivity'] = data.appActivityName
    #desired_caps['appWaitPackage'] = data.appWaitPackageName
    #Adding appWait Activity since the activity name changes as the focus shifts to the ATP WTA app's first page
    #desired_caps['appWaitActivity'] = data.appWaitActivityName
    desired_caps['appWaitDuration'] ='50000' 
    desired_caps['noReset '] = 'true'
    desired_caps['fullReset'] = 'false'
    desired_caps['autoGrantPermissions'] = 'true'
    desired_caps['ignoreHiddenApiPolicyError'] = 'true'
    return desired_caps       
    
def getDriver():
    return webdriver.Remote('http://127.0.0.1:4723/wd/hub', capabilities())
 
def tearDown(driver):
    driver.quit()


def start_screen_record(driver,logger):
    driver.start_recording_screen()
    logger.info("****Start Recording the App Screen****")

def stop_screen_record(driver, logger): 
    screen_record=driver.stop_recording_screen()
    video_Name=driver.current_activity+time.strftime("%Y_%m_%d_%H%M%S")
    fileName = os.path.join('/Phone/Pictures/Screenshots/',video_Name+".mp4")
    
    with open(fileName, 'wb') as vd:
        vd.write(base64.b64decode(screen_record))
    logger.info("****screen recording stored in the following path screenrecordings\\"+video_Name+".mp4"+"****")
    
def savescreenshot(driver,name):
    file_name=driver.current_activity+time.strftime("%Y_%m_%d_%H%M%S")
    create_file(screenshots,name+_+file_name+".png")
    driver.save_screenshot(create_file)    






        


