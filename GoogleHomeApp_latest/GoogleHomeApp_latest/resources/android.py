import subprocess
def device_info(command):
    #return os.system(command)
    device_info=subprocess.Popen(command, shell=True)
    return device_info.communicate()
      
def getAndroidVersion():
    device_info('adb shell getprop ro.build.version.release')
    
def getDeviceName():
    device_info('adb shell getprop ro.product.model')

def getDeviceUUID():
    device_info('adb shell getprop ro.serialno')
    
def get_current_activity(driver):
    activity = driver.current_activity
    return activity
