import os
import sys
import time


def nmap():
	print '\n###### Installing Nmap'
	os.system('apt update && apt upgrade')
	os.system('apt install nmap')
	print '###### Done'
	print "###### Type 'nmap' to start."

def red_hawk():
	print '\n###### Installing RED HAWK'
	os.system('apt update && apt upgrade')
	os.system('apt install git php')
	os.system('git clone https://github.com/Tuhinshubhra/RED_HAWK')
	os.system('mv RED_HAWK ~')
	print '###### Done'
	
def dtect():
	print '\n###### Installing D-Tect'
	os.system('apt update && apt upgrade')
	os.system('apt install python2 git')
	os.system('git clone https://github.com/shawarkhanethicalhacker/D-TECT')
	os.system('mv D-TECT ~')
	print '###### Done'

def sqlmap():
	print '\n###### Installing sqlmap'
	os.system('apt update && apt upgrade')
	os.system('apt install git python2')
	os.system('git clone https://github.com/sqlmapproject/sqlmap')
	os.system('mv sqlmap ~')
	print '###### Done'

def infoga():
	print '\n###### Installing Infoga'
	os.system('apt update && apt upgrade')
	os.system('apt install python2 git')
	os.system('pip2 install requests urllib3 urlparse')
	os.system('git clone https://github.com/m4ll0k/Infoga')
	os.system('mv Infoga ~')
	print '###### Done'

def reconDog():
	print '\n###### Installing ReconDog'
	os.system('apt update && apt upgrade')
	os.system('apt install python2 git')
	os.system('git clone https://github.com/UltimateHackers/ReconDog')
	os.system('mv ReconDog ~')
	print '###### Done'
	backtomenu_option()

def androZenmap():
	print '\n###### Installing AndroZenmap'
	os.system('apt update && apt upgrade')
	os.system('apt install nmap curl')
	os.system('curl -O http://override.waper.co/files/androzenmap.txt')
	os.system('mkdir ~/AndroZenmap')
	os.system('mv androzenmap.txt ~/AndroZenmap/androzenmap.sh')
	print '###### Done'

def sqlmate():
	print '\n###### Installing sqlmate'
	os.system('apt update && apt upgrade')
	os.system('apt install python2 git')
	os.system('pip2 install mechanize bs4 HTMLparser argparse requests urlparse2')
	os.system('git clone https://github.com/UltimateHackers/sqlmate')
	os.system('mv sqlmate ~')
	print '###### Done'
	
def astraNmap():
	print '\n###### Installing AstraNmap'
	os.system('apt update && apt upgrade')
	os.system('apt install git nmap')
	os.system('git clone https://github.com/Gameye98/AstraNmap')
	os.system('mv AstraNmap ~')
	print '###### Done'

def wtf():
	print '\n###### Installing WTF'
	os.system('apt update && apt upgrade')
	os.system('apt install git python2')
	os.system('pip2 bs4 requests HTMLParser urlparse mechanize argparse')
	os.system('git clone https://github.com/Xi4u7/wtf')
	os.system('mv wtf ~')
	print '###### Done'
