import unittest
from selenium.webdriver.common.by import By
from resources import data
from datetime import datetime
from resources import base
from resources import testCases
from resources import android
from datetime import datetime
import time
import os
import LSDevice
import pyfiglet
import logging


now = datetime.now()
sp=os.sep
run_string = now.strftime("%d%m%Y")

def writeToFileRunStatus(filename,Content):
    with open(filename+'_'+run_string+'.txt','a') as runstatus:
        runstatus.write(Content+'\r\n')
        
def GoogleHomeApp(i):
    font= pyfiglet.figlet_format('Google Home Setup')
    print(font)
    
    dt_string = now.strftime("%d%m%Y-%H%M%S")

    errorList=['what are you setting up','Could not Communicat with your device', 'Somthing Went Wrong','Turn Off Ap Isolation','Connection problem during setup', 'Device wifi Setup Pass']
    "Class to run tests against the GoogleHomeApp App "
     
    #Create and configure logger
    tm=datetime.now().strftime("%m-%d-%Y %H%M%S")
    logging.basicConfig(filename=base.create_file("logs" ,"GoogleHomeApp_Automation_logs"+tm+".log"),
                    format='%(asctime)s %(message)s',
                    filemode='a')
    #Creating an object
    logger=logging.getLogger()
  
    
    logger.setLevel(logging.INFO)
    
    
    logger.info("********Appium Server Starting********")
    base.start_appium_server()
    
    android_driver=base.getDriver()
    
    
    
    logger.info("********Android Driver created********")
    #base.start_screen_record(android_driver,logger)
    
      
    logger.info("*********LS10 Device Setup beggining*********")
    android_driver.implicitly_wait(30)
    
    try:
        errorString=testCases.Google_home_setup(android_driver,logger)
        if errorString.lower() == errorList[0].lower():
            LSDevice.SetFacDefault()
            time.sleep(2)
            writeToFileRunStatus('GoogleHomeSetup','DeviceNotSound_'+'run'+str(i)+' '+'='+' None')
        if errorString.lower() == errorList[1].lower():
            LSDevice.captureLogs('Could_not_comm_with_your_device_'+'run'+str(i))
            time.sleep(0.5)
            LSDevice.SetFacDefault()
            time.sleep(2)
            writeToFileRunStatus('GoogleHomeSetup','Could_not_comm_with_your_device_'+'run'+str(i)+' '+'='+' Setup Failed')
        if errorString.lower() == errorList[2].lower():
            LSDevice.captureLogs('Something_went_wront'+'run'+str(i))
            time.sleep(0.5)
            LSDevice.SetFacDefault()
            time.sleep(2)
            writeToFileRunStatus('GoogleHomeSetup','Something_went_wront'+'run'+str(i)+' '+'='+' '+' Cast Link Failed on post wifi setup')
        if errorString.lower() == errorList[3].lower():
            LSDevice.captureLogs('Turn_off_ap_isolation'+'run'+str(i))
            time.sleep(0.5)
            LSDevice.SetFacDefault()
            time.sleep(2)
            writeToFileRunStatus('GoogleHomeSetup','Turn_off_ap_isolation'+'run'+str(i)+' '+'='+' Cast Link Failed on post wifi setup')
        if errorString.lower() == errorList[4].lower():
            LSDevice.captureLogs('Connection_problem_during_setup'+'run'+str(i))
            time.sleep(0.5)
            LSDevice.SetFacDefault()
            time.sleep(2)
            writeToFileRunStatus('GoogleHomeSetup','Connection_problem_during_setup'+'run'+str(i)+' '+'='+' Found PSK Key error')
        if 'Device wifi Setup Pass'.lower() == errorList[5].lower():
            time.sleep(0.5)
            LSDevice.SetFacDefault()
            time.sleep(2)
            writeToFileRunStatus('GoogleHomeSetup','Wifi Setup Successfull'+'run'+str(i)+' '+'='+' Setup PASS')
        
    except Exception:
        print('ERROR IN YOUR TEST PLEASE VERIFY IT')
    #base.stop_screen_record(android_driver,logger)    
    base.stop_appium_server()

#---START OF SCRIPT
if __name__ == '__main__':
    for i in range(0,100):
        GoogleHomeApp(i)