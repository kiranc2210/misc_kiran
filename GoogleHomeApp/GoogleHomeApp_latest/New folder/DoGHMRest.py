import unittest
from selenium.webdriver.common.by import By
from resources import data
from datetime import datetime
from resources import base
from resources import resettest
from resources import android
from datetime import datetime
import time
import os
import GHMDevice
import pyfiglet
import logging


now = datetime.now()
sp=os.sep
run_string = now.strftime("%d%m%Y")

        
def GoogleHomeApp():
    print('\r\n')
    font= pyfiglet.figlet_format('Google Home Setup')
    print(font)
    
    dt_string = now.strftime("%d%m%Y-%H%M%S")

    errorList=['what are you setting up','Could not Communicat with your device', 'Somthing Went Wrong','Turn Off Ap Isolation','Connection problem during setup', 'Device wifi Setup Pass', 'No Device Found']
    "Class to run tests against the GoogleHomeApp App "
     
    #Create and configure logger
    tm=datetime.now().strftime("%m-%d-%Y %H%M%S")
    logging.basicConfig(filename=base.create_file("logs" ,"GoogleHomeAppGHM_Automation_logs"+tm+".log"),
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
        errorString=resettest.Google_home_mini_reset(android_driver,logger)
        return 'Successfull'
    except Exception:
        print('ERROR IN YOUR TEST PLEASE VERIFY IT')
    

#---START OF SCRIPT
if __name__ == '__main__':
        time.sleep(5)
        try:
            base.start_appium_server()
            GoogleHomeApp()
            base.stop_appium_server()
        except:
            time.sleep(5)
            base.start_appium_server()
            GoogleHomeApp()
            base.stop_appium_server()