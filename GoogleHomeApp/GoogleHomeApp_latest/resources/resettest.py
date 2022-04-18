from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from appium.webdriver.common.touch_action import TouchAction
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from resources import base
from resources import tests
import time
import os  


    
        
    
def Google_home_mini_reset(driver,logger):
    try:
        tests.getStarted(driver,logger)
        try: 
            print('Entering to Chooce a Home screen')
            tests.Choose_account(driver,logger)
        except:
            print('Failed to click on Next Button in Choose Home Screen, try again choose account')
            tests.Choose_account(driver,logger)
        try:
            tests.click_plus_icon_to_continue_to_setup(driver,logger)
        except:
            pass
    except:
        print("error in script")
