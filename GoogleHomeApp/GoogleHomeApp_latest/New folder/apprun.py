import subprocess
try:
    ping=subprocess.Popen('py GoogleHomeApp.py',stdout = subprocess.PIPE,stderr = subprocess.PIPE,shell=True)
    out = ping.communicate()
    print(str(out))
except:
    ping=subprocess.Popen('py GoogleHomeApp.py',stdout = subprocess.PIPE,stderr = subprocess.PIPE,shell=True)
    out = ping.communicate()
    print(str(out))