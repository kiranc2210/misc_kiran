from appium import webdriver
from selenium.webdriver.common.by import By
from appium.webdriver.common.touch_action import TouchAction
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def wait_for_element_to_be_clickable(driver, locator, elem, sleep=10):
    eleme = WebDriverWait(driver, sleep).until(EC.element_to_be_clickable((By.locator, elem)))
    return eleme
        
def wait_for_element_to_be_located(driver, locator, elem, sleep=10):
    eleme = WebDriverWait(driver, sleep).until(EC.presence_of_element_located((By.locator, elem)))
    return eleme
           
def tap_on_element(driver, element, sleep=3):
    actions = TouchAction(driver)
    actions.tap(element)
    actions.perform()
    
def touchElementByCoordinate(driver,x,y):
    TouchAction(driver).tap(None, x, y, 1).perform()
 
def Scroll_To_Element_click(driver, element_txt):
    targetElement = driver.find_element_by_android_uiautomator('new UiScrollable(new UiSelector().scrollable(true).instance(0)).scrollIntoView(new UiSelector().text("element_txt").instance(0))')
    targetElement.click()

def getText(driver, element):
    return driver.element.text

def scroll_up():
    _y_scroll(scroll_y_top,scroll_y_bottom)

def scroll_down():
    _y_scroll(scroll_y_bottom, scroll_y_top)

def _y_scroll(y_start, y_end):
    SCROLL_DUR_MS = 3000
    window_size = driver.get_window_size()
    
    scroll_y_top = window_size['height'] * 0.2
    scroll_y_bottom = window_size['height'] * 0.8
    scroll_x = window_size['width'] * 0.5
    
    actions = TouchAction(driver)
    actions.long_press(None, scroll_x, y_start, SCROLL_DUR_MS)
    actions.move_to(None, scroll_x, y_end)
    actions.perform()