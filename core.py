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
time.sleep(1)

print '\n###### Installing sqlmap'
os.system('apt update && apt upgrade')
os.system('apt install git python2')
os.system('git clone https://github.com/sqlmapproject/sqlmap')
os.system('mv sqlmap ~')
print '###### Done'
time.sleep(1)


print '\n###### Installing Infoga'
os.system('apt update && apt upgrade')
os.system('apt install python2 git')
os.system('pip2 install requests urllib3 urlparse')
os.system('git clone https://github.com/m4ll0k/Infoga')
os.system('mv Infoga ~')
print '###### Done'
time.sleep(1)

print '\n###### Installing ReconDog'
os.system('apt update && apt upgrade')
os.system('apt install python2 git')
os.system('git clone https://github.com/UltimateHackers/ReconDog')
os.system('mv ReconDog ~')
print '###### Done'
time.sleep(1)

print '\n###### Installing AndroZenmap'
os.system('apt update && apt upgrade')
os.system('apt install nmap curl')
os.system('curl -O http://override.waper.co/files/androzenmap.txt')
os.system('mkdir ~/AndroZenmap')
os.system('mv androzenmap.txt ~/AndroZenmap/androzenmap.sh')
print '###### Done'
time.sleep(1)

print '\n###### Installing WTF'
os.system('apt update && apt upgrade')
os.system('apt install git python2')
os.system('pip2 bs4 requests HTMLParser urlparse mechanize argparse')
os.system('git clone https://github.com/Xi4u7/wtf')
os.system('mv wtf ~')
print '###### Done'
time.sleep(1)












