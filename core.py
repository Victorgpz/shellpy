import os
import sys
import time
print "\n vic's tools \n"

print '\n###### Installing Nmap'
os.system('apt update && apt upgrade')
os.system('apt install nmap')
print '###### Done'
print "###### Type 'nmap' to start."
time.sleep(10)

