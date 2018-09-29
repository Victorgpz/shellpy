import os

import sys

from time import sleep as timeout
from cy.py import *

def main():
print "\n vic's tools \n"
print "\n [01] Nmap"
print " [02] Red Hawk"
print " [03] D-Tect"
print " [04] sqlmap"
print " [05] Infoga"
print " [06] ReconDog"
print " [07] AndroZenmap"
print " [08] sqlmate"
print " [09] AstraNmap"
print " [10] WTF"
infogathering=raw_input("vic >>")
       
if infogathering == "01" or infogathering == "1":
       nmap()
elif infogathering == "02" or infogathering == "2":
			red_hawk()
elif infogathering == "03" or infogathering == "3":
			dtect()
elif infogathering == "04" or infogathering == "4":
			sqlmap()
elif infogathering == "05" or infogathering == "5":
			infoga()
elif infogathering == "06" or infogathering == "6":
			reconDog()
elif infogathering == "07" or infogathering == "7":
       androZenmap()
elif infogathering == "08" or infogathering == "8":
       sqlmate()
elif infogathering == "09" or infogathering == "9":
			astraNmap()
elif infogathering == "10":
			wtf()