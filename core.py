import os
import sys
import time
print "\n vic's tools \n"

print '\n###### Installing Nmap'
os.system('apt update && apt upgrade')
os.system('apt install nmap')
print '###### Done'
print "###### Type 'nmap' to start."
time.sleep(1)

print '\n###### Installing RED HAWK'
os.system('apt update && apt upgrade')
os.system('apt install git php')
os.system('git clone https://github.com/Tuhinshubhra/RED_HAWK')
os.system('mv RED_HAWK ~')
print '###### Done'
time.sleep(.500)

print '\n###### Installing D-Tect'
os.system('apt update && apt upgrade')
os.system('apt install python2 git')
os.system('git clone https://github.com/shawarkhanethicalhacker/D-TECT')
os.system('mv D-TECT ~')
print '###### Done' 
time.sleep(.500)



