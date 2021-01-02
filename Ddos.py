import time
import os
from sys import exit

##############################
#~~~~~~~~~~Color~~~~~~~~~~~~#
##############################

Green = '\033[92m'
Yellow = '\033[93m'
Red = '\033[91m'
Blue = '\033[94m'
Puple = '\033[95m'
Dam = '\033[1m'
Mong = '\033[0m'
Gach = '\033[4m'
In_dam_1 = '\033[3m'
In_dam_2 = '\033[41m' #In dam do
In_dam_3 = '\033[42m' #In dam xanh la
In_dam_4 = '\033[43m' #In dam vang
In_dam_5 = '\033[44m' #In dam xanh bien
In_dam_6 = '\033[45m' #In dam tim
In_dam_7 = '\033[46m' #In dam xanh troi
In_dam_8 = '\033[47m' #In dam trang
Trong = '\033[8m'
Black = '\033[30m'
Blue_sky = '\033[36m'
White = '\033[37m'
Special = '\033[11m'

##############################
#~~~~~~~~~~~~~~~~~~~~~~~~~#
#############################

os.system('clear')
def title():
     print(Dam + Yellow + "############################################")
     print("<<<~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~>>>")
     print("<<<                                      >>>")
     print("<<<" + Puple +"   8888b.   8888b.    dP~YP  .dP~Y8" + Yellow + "   >>>")
     print("<<<" + Puple + "    8I  Yb   8I  Yb  dP   YP 'Ybo,'" + Yellow + "   >>>")
     print("<<<" + Puple + "    8I  dY   8I  dY  YP   dP o.'YBb" + Yellow + "   >>>")
     print("<<<" + Puple + "   8888Y'   8888Y'    YbcdP  8bodP'" + Yellow+ "   >>>")
     print(Yellow + "<<<                                      >>>")
     print( "<<<~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~>>>")
     print( "############################################")
     print("<<<    " + Red + "Čreated by ĞuenHataraku / v2.0" + Yellow + "    >>>")
     print("<<< Facebook: Công Otaku                 >>>")
     print("<<< Github:                              >>>")
     print("<<< Discord:                             >>>")
     print( "############################################")
##############################
#~~~~~~~~~~~~~~~~~~~~~~~~~#
#############################
     
password = ' '
while password != 'ddos':
     print(Dam + Green + "<~~~Password~~~>")
     password = input('[?]~~>' + Red)
os.system('clear')

#########################################
title()#~~~>Menu<~~~#
print(Dam + Yellow + "<~~~~~~~~~~~Menu~~~~~~~~~~>")
print("<                         >")
print("<" + Dam + Blue_sky + "   [0]~~>" + Mong + Green + "Ddos" + Yellow + "            >")
print("<" + Dam + Blue_sky + "   [1]~~>" + Mong + Green + "Update" + Yellow + "          >")
print("<" + Dam + Blue_sky + "   [2]~~>" + Mong + Green + "Exit" + Yellow + "            >")
print("<                         >")
print("<~~~~~~~~~~~~~~~~~~~~~~~~~>\n")
n = int(input(Dam + Blue + "[?]~~> Select: "))
########################################

os.system('clear')
if n == 0:
     title() #~~~Select 0
     host = input(Red + '[1]~~>Target: ' + Green)
     ip = input(Red + '[2]~~>IP address: ' + Green)
     port = input(Red + '[3]~~>Port: ' + Green)
     i = 1
     while True:
          time.sleep(0.1)
          print(Green + "Send package " + Red + "~> " + Green + str(i) + " bytes " + Red + "~> " + Green + "IP address " + str(ip) + "/ port " + port)
          i += 1
elif n == 1:
     title() #~~~Select 1
     print(Green + "\nChecking update....")
     time.sleep(1)
     print("\tNo have update version...")
else:
     title() #~~~Select 2
     print(Yellow + 'Thank for using')
     print("\tStop program\n" + Green)
     time.sleep(1)
     exit()
     
'''  Note
\n = \v = \f : down line
\t : create space white
'''