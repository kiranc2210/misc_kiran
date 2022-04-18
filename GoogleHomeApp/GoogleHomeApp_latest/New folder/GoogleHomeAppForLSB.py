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
    time.sleep(5)
    LSDevice.SetFacDefault()
    time.sleep(2)
    with open(filename+'_'+run_string+'.txt','a') as runstatus:
        runstatus.write(Content+'\r\n')
        


        
def GoogleHomeApp(i):
    print('\r\n')
    font= pyfiglet.figlet_format('Google Home Setup')
    print(font)
    
    dt_string = now.strftime("%d%m%Y-%H%M%S")

    errorList=['what are you setting up','Could not Communicat with your device', 'Somthing Went Wrong','Turn Off Ap Isolation','Connection problem during setup', 'Device wifi Setup Pass', 'No Device Found']
    "Class to run tests against the GoogleHomeApp App "
     
    #Create and configure logger
    tm=datetime.now().strftime("%m-%d-%Y %H%M%S")
    logging.basicConfig(filename=base.create_file("logs" ,"GoogleHomeAppLS_Automation_logs"+tm+".log"),
                    format='%(asctime)s %(message)s',
                    filemode='a')
    #Creating an object
    logger=logging.getLogger()
  
    
    logger.setLevel(logging.INFO)
    
    
    logger.info("********Appium Server Starting********")
    #base.start_appium_server()
    
    android_driver=base.getDriver()
    
    
    
    logger.info("********Android Driver created********")
    #base.start_screen_record(android_driver,logger)
    
      
    logger.info("*********LS10 Device Setup beggining*********")
    android_driver.implicitly_wait(30)
    try:
        errorString=testCases.Google_home_setup(android_driver,logger)
        if errorString.lower() == errorList[0].lower():
            writeToFileRunStatus('GoogleHomeSetupLS', 'GoogleHomeSetup_Run'+str(i)+' '+'='+' '+'what are you setting up')
        if errorString.lower() == errorList[1].lower():
            LSDevice.captureLogs('Could_not_comm_with_your_device_'+'run'+str(i))
            writeToFileRunStatus('GoogleHomeSetupLS', 'GoogleHomeSetup_Run'+str(i)+' '+'='+' '+'Could not Communicat/Authenticate with your device')
        if errorString.lower() == errorList[2].lower():
            LSDevice.captureLogs('Something_went_wront_'+'run'+str(i))
            writeToFileRunStatus('GoogleHomeSetupLS', 'GoogleHomeSetup_Run'+str(i)+' '+'='+' '+'Somthing Went Wrong')
        if errorString.lower() == errorList[3].lower():
            LSDevice.captureLogs('Turn_off_ap_isolation_'+'run'+str(i))
            writeToFileRunStatus('GoogleHomeSetupLS', 'GoogleHomeSetup_Run'+str(i)+' '+'='+' '+'Turn Off Ap Isolation')
        if errorString.lower() == errorList[4].lower():
            LSDevice.captureLogs('Connection_problem_during_setup_'+'run'+str(i))
            writeToFileRunStatus('GoogleHomeSetupLS', 'GoogleHomeSetup_Run'+str(i)+' '+'='+' '+'Connection_problem_during_setup/PSK/wrong password issue')
        if errorString.lower() == errorList[5].lower():
            LSDevice.captureLogs('SuccessfullWIFI Setup_ '+'run'+str(i))
            writeToFileRunStatus('GoogleHomeSetupLS', 'GoogleHomeSetup_Run'+str(i)+' '+'='+' '+' Setup PASS')
        if errorString.lower() == errorList[6].lower():
            LSDevice.captureLogs('No Device Found_ '+'run'+str(i))
            writeToFileRunStatus('GoogleHomeSetupLS', 'GoogleHomeSetup_Run'+str(i)+' '+'='+' '+' No Device Found. Make sure device are turned on and available to connect.')
        base.tearDown(android_driver)
    except Exception:
        time.sleep(5)
        LSDevice.SetFacDefault()
        time.sleep(2)
        print('ERROR IN YOUR TEST PLEASE VERIFY IT')
    

#---START OF SCRIPT
if __name__ == '__main__':
    for i in range(200):
        time.sleep(5)
        try:
            base.start_appium_server()
            GoogleHomeApp(i)
            base.stop_appium_server()
        except:
            time.sleep(5)
            base.start_appium_server()
            GoogleHomeApp(i)
            base.stop_appium_server()