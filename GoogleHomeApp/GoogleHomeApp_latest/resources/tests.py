from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from appium.webdriver.common.touch_action import TouchAction
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from resources import base
from resources import action,locators,android,data,testCases
from appium.webdriver.common.touch_action import TouchAction
import time
import os 
from datetime import datetime
now = datetime.now()
sp=os.sep
run_string = now.strftime("%d%m%Y")

def getStarted(driver,logger):
    getStarted_btn=WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.ID, locators.get_started_btn)))
    logger.info('Hurry Google Home app Launched Successfully and Staretd automating the App')
    action.tap_on_element(driver,getStarted_btn)
    print('Hurry Google Home app Launched Successfully and Staretd automating the App')
    print('Click on Get Started')
    
def Choose_account(driver,logger):
    time.sleep(2)    
    choose_account=WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.ANDROID_UIAUTOMATOR, locators.choose_account)))
    logger.info("Choose a Account You will be able to control the devices and Services in this Home")
    action.tap_on_element(driver,choose_account)
    print('Choose a Account You will be able to control the devices and Services in this Home')
    time.sleep(10)
    choose_account_on_btn=WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.ANDROID_UIAUTOMATOR, locators.choose_account_on_btn)))
    logger.info("'Click on OK button in Choose a Account screen'")
    action.tap_on_element(driver,choose_account_on_btn)
    print('Click on OK button in Choose a Account screen')
    click_next=WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.ANDROID_UIAUTOMATOR, locators.Next_btn)))
    logger.info("*********click on"+" "+click_next.text+"*********")
    action.tap_on_element(driver,click_next)
   
    
def click_plus_icon_to_continue_to_setup(driver, logger):
    click_plus_icon=WebDriverWait(driver, 1).until(EC.presence_of_element_located((By.ID, locators.click_plus_icon)))
    logger.info("click on Plus icon on Home")
    action.tap_on_element(driver,click_plus_icon)
    print("click on Plus icon on Home")
    
    time.sleep(10)
    action.touchElementByCoordinate(driver, 334, 482)
    print('Click on Setup a Device')
    logger.info("Click on Setup a Device")
 
    time.sleep(10)
    action.touchElementByCoordinate(driver, 410, 915)
    print("click on New Device")
    logger.info("click on New Device")
    try:
        click_next=WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.ANDROID_UIAUTOMATOR, locators.Next_btn)))
        logger.info("*********click on"+" "+click_next.text+"*********")
        action.tap_on_element(driver,click_next)
        print("click on next Button Choose a home screen ")
        logger.info("click on next Button Choose a home screen ")
    except:
        pass
   
       
def device_discovery(driver, logger):
    try:
        try:
            friendly_name=WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.ANDROID_UIAUTOMATOR, locators.frienldyName)))
            logger.info("selecting the FriendlyName"+':'+data.FriendlyName+" in the list of Device")
            action.tap_on_element(driver,friendly_name)
            print("selecting the FriendlyName"+':'+data.FriendlyName+" in the list of Device")
            click_next_btn=WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.ANDROID_UIAUTOMATOR, locators.Next_btn)))
            logger.info('click on next button in the NearBy Devices Screen')
            action.tap_on_element(driver, click_next_btn)
            print('click on next button in the NearBy Devices Screen')
            return 'pass' 
        except:
            actions = TouchAction(driver)
            actions.press(el=None, x=280, y=1222).move_to(el=None, x=277, y=617).release().perform()
            friendly_name=WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.ANDROID_UIAUTOMATOR, locators.frienldyName)))
            logger.info("selecting the FriendlyName"+':'+data.FriendlyName+" in the list of Device")
            action.tap_on_element(driver,friendly_name)
            print("selecting the FriendlyName"+':'+data.FriendlyName+" in the list of Device")
            click_next_btn=WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.ANDROID_UIAUTOMATOR, locators.Next_btn)))
            logger.info('click on next button in the NearBy Devices Screen')
            action.tap_on_element(driver, click_next_btn)
            print('click on next button in the NearBy Devices Screen')
            return 'pass' 
    except:
         discovery_title=WebDriverWait(driver, 30).until(EC.presence_of_element_located((By.ANDROID_UIAUTOMATOR, locators.Lyric_Speaker_Box)))
         if discovery_title.text == 'Lyric Speaker Box found':
             yes_btn=WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.ANDROID_UIAUTOMATOR, locators.yes_btn)))
             logger.info("clck on yes button in the Lyric Speaker Box found screen")
             action.tap_on_element(driver,yes_btn)
             print('clck on yes button in the Lyric Speaker Box found screen')
             return 'pass'
             
       
            
            
def post_device_discovery(driver, logger):
    errorsrt="We couldn\'t authenticate your Lyric Speaker Box. Please visit support.google.com/chromecast for help troubleshooting this issue."
    '''try:
        couldnotauthenticate=WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ANDROID_UIAUTOMATOR, locators.could_not_authenticate)))
        print('Could not Authenticate')
        if couldnotauthenticate.text== errorsrt:
            Logger.info('Found Could not authenticate/Communicate with you device during the Google Home app try to communicate with LS Devices')
            #action.tap_on_element(driver, locators.alrt_OK_btn)
            return 'Could not Communicat with your device'
    except:
        pass'''
        
    setup_tone_yes_btn=WebDriverWait(driver, 60).until(EC.presence_of_element_located((By.ANDROID_UIAUTOMATOR, locators.Did_you_hear_the_sound_yes_btn)))
    logger.info('Did you hear setup tone and Click on yes button')
    action.tap_on_element(driver,setup_tone_yes_btn)
    print('Did you hear setup tone and Click on yes button')
        
        
    yes_im_in_btn=WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.ANDROID_UIAUTOMATOR, locators.yes_im_in)))
    logger.info("click on Yes i\'m in button in the Help to setup device")
    action.tap_on_element(driver, yes_im_in_btn)
    print("click on Yes i\'m in button in the Help to setup device") 
            
    where_is_this_device_=WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.ANDROID_UIAUTOMATOR, locators.Where_is_this_device)))
    logger.info('We are in Where is this Device? Screen & click on Room Name')
    print('We are in Where is this Device? Screen')
    if where_is_this_device_.text == 'Where is this device?':
        time.sleep(2)
        action.touchElementByCoordinate(driver, 307, 1096)
        print('click on Room Name')
       
            
    click_next_btn=WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.ANDROID_UIAUTOMATOR, locators.Next_btn)))
    logger.info("Room Name Selected now click on next button to redirect to WIFI SSID list")
    action.tap_on_element(driver, click_next_btn)
    print("click on next button")
    
    try:
        wifi_pwd_selection(driver, logger)
        #return 'pass'       
         
    except:
        create_a_uniquesName=WebDriverWait(driver, 2).until(EC.presence_of_element_located((By.ANDROID_UIAUTOMATOR, locators.create_a_unique_name)))
        print("we are in Create a unique Nacme screen")
        if 'Create a unique name'.lower() in driver.page_source.lower():
            click_next_btn=WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.ANDROID_UIAUTOMATOR, locators.Next_btn)))
            logger.info("we are in Create a unique Nacme screen, click on next Button")
            action.tap_on_element(driver, click_next_btn)
            print('click on next Button')
        wifi_pwd_selection(driver, logger) 
            #return 'pass'
       
           
def wifi_pwd_selection(driver, logger):
                        
    select_ssid=WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.ANDROID_UIAUTOMATOR, locators.ssid_name)))
    print('Selecting ssid from SSID list')

    if select_ssid.text == data.wifissid:
        action.tap_on_element(driver, select_ssid)
        print('click on ssid'+ data.wifissid)
        click_next_btn=WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ANDROID_UIAUTOMATOR, locators.Next_btn)))
        logger.info('SSID Selected'+':'+data.wifissid+'clicked next button in the List Of ssid Screen')
        action.tap_on_element(driver, click_next_btn)
        print('clicked next button in the List Of ssid Screen')
    else:
        action.Scroll_To_Element_click(driver, select_ssid)
    try:
        #WiFi_password=WebDriverWait(driver, 2).until(EC.presence_of_element_located((By.ANDROID_UIAUTOMATOR, locators.enter_wifi_password)))
        #print(WiFi_password.text)
        #logger.info("Enter Password:"+" "+WiFi_password.text)
        pwd_txt=WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.ANDROID_UIAUTOMATOR, locators.Wi_Fi_password)))
        pwd_txt.send_keys(data.wifiPassword)
        print('ented the Password'+data.wifiPassword)
        click_next_btn=WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.ANDROID_UIAUTOMATOR, locators.Connect_btn)))
        logger.info('click on Next Button')
        action.tap_on_element(driver, click_next_btn)
        print('click on Next Button')
    except:
        click_OK_btn=WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.ANDROID_UIAUTOMATOR, locators.pwd_OK_btn)))
        logger.info("Password remembered by the Google Home app Click ok to proceed to Linking to Cast")
        action.tap_on_element(driver, click_OK_btn)
        print('Password remembered by the Google Home app Click ok to proceed to Linking to Cast')

        

def linking_to_cast(driver, logger):
    try:
        Linking_your_SFLEX101=WebDriverWait(driver,60).until(EC.presence_of_element_located((By.ANDROID_UIAUTOMATOR,locators.Linking_your_SFLEX101)))
        print('found successfully Linking_your_Lyric Speaker BOX screen')
    except:
        print('observed either Turnoff AP Isolation on Soemthing went wrong issue') 
        if 'Somthing Went wrong'.lower() in driver.page_source.lower():
            driver.get_screenshot_as_file('{0}.jpg'.format('SomethingWentWrong'+'-'+run_string))
            print('Found Something went wrong')
            logger.info("Found Something went wrong error popup")
            return 'Somthing Went Wrong'
       
        if 'Turn off AP isolation'.lower() in driver.page_source.lower():
            driver.get_screenshot_as_file('{0}.jpg'.format('TurnOffAPIsolation'+'-'+run_string))
            print('Found Turn off AP isolation')
            logger.info("Found Turn off AP isolation error popup")
            return 'Turn Off Ap Isolation'
        
        if 'Connection problem during setup'.lower() in driver.page_source.lower():
            driver.get_screenshot_as_file('{0}.jpg'.format('ConnectionProblemDuringSetup'+'-'+run_string))
            print('Found Connection problem during setup PWD key error poup')
            return 'Connection problem during setup'
            
        if 'No Device Found. Make sure device are turned on and available to connect.'.lower() in driver.page_source.lower():
            return 'No Device Found'
                
    if Linking_your_SFLEX101.text == 'Linking your Lyric Speaker Box':
        click_next_btn=WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.ANDROID_UIAUTOMATOR, locators.Next_btn)))
        action.tap_on_element(driver, click_next_btn)
        logger.info("click on next button in the Linking your Lyric Speaker fox screen")
        print('click on next button in the Linking your Lyric Speaker fox screen')

        Continue_btn=WebDriverWait(driver, 60).until(EC.presence_of_element_located((By.ANDROID_UIAUTOMATOR, locators.Continue_btn)))
        action.tap_on_element(driver, Continue_btn)
        logger.info("click on Continue button")
        print('click on Continue button')
        try:
            Continue_btn1=WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ANDROID_UIAUTOMATOR, locators.Continue_btn)))
            action.tap_on_element(driver, Continue_btn1)
            logger.info("click on continue button")
            print('click on continue button')                
           
            skip_tutorial_link=WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ANDROID_UIAUTOMATOR, locators.skip_tutorial_)))
            action.tap_on_element(driver, skip_tutorial_link)
            print('click on skip tutorials')
            logger.info("click on skip tutorials")
            print('Google Home Setup Successfull')
            logger.info("Google Home Setup Successfull")
            return 'Device wifi Setup Pass'
        except:
            updating_OTA=WebDriverWait(driver, 80).until(EC.invisibility_of_element_located((By.ANDROID_UIAUTOMATOR, locators.updateota)))
            action.tap_on_element(driver, updating_OTA)

            Continue_btn1=WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ANDROID_UIAUTOMATOR, locators.Continue_btn)))
            action.tap_on_element(driver, Continue_btn1)
            print('click on continue button')
            logger.info("click on continue button")            
           
            skip_tutorial_link=WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ANDROID_UIAUTOMATOR, locators.skip_tutorial_)))
            action.tap_on_element(driver, skip_tutorial_link)
            print('click on skip tutorials')
            logger.info("click on skip tutorials")
            print('Google Home Setup Successfull')
            logger.info("Google Home Setup Successfull")
            return 'Device wifi Setup Pass'
            
 

#def doNetWorkResetFromGHApp(driver, logger):
 
  
 
 
        