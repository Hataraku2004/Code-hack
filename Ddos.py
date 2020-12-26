import time
import os
import system

#~~~~~~~~Color~~~~~~~~~~~#
Green = '\033[92m'
Yellow = '\033[93m'
Red = '\033[91m'
Blue = '\033[94m'
Pink = '\033[95m'
Dam = '\033[1m'
Mong = '\033[0m'
Gach = '\033[4m'
In_dam = '\033[3m'
Trong = '\033[8m'
Black = '\033[30m'
Blue_sky = '\033[36m'
White = '\033[37m'
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~#
os.system('clear')
print(Dam + Yellow +"<<<~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~>>>")
print("<<<                                      >>>")
print("<<<" + Pink +"  8888b.   8888b.    dP~YP  .dP~Y8" + Yellow + "    >>>")

print("<<<" + Pink + "   8I  Yb   8I  Yb  dP   YP 'Ybo,'" + Yellow + "    >>>")

print("<<<" + Pink + "   8I  dY   8I  dY  YP   dP o.'YBb" + Yellow + "    >>>")

print("<<<" + Pink + "  8888Y'   8888Y'    YbcdP  8bodP'" + Yellow+ "    >>>")

print(Yellow + "<<<                                      >>>")
print("<<<~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~>>>")
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~#
print('############################################')
print(Dam + Red + "#   ~~~~~~~~~>|\/| E |\| |_|<~~~~~~~~~~   #")
print(Yellow + '############################################')
print('\n')
print(Green + "Created by " + White + "GuenHataraku " + Green +"/ Ddos v1.0")
print("\n")
print(Mong + Blue_sky + "[0]~~>" + Dam + Green + " Ddos")
print(Mong + Blue_sky + "[1]~~>" + Dam + Green + " Update")
print(Mong + Blue_sky + "[2]~~>" + Dam + Green + " Exit")

n = int(input(Dam + Blue + "\n"+ "~~> Select: "))
os.system('clear')
if n == 0:
     host = input(Red + '[1]~~>Target: ')
     ip = input('[2]~~>IP address: ')
     port = input('[3]~~>Port: ')
     i = int(input("[4]~~>Press byte need send: "))
     while i >= 0:
          time.sleep(0.3)
          print(Green + "Send package => " + str(i) + " bytes to IP address " + str(ip))
          i += 1
          if i % 100 == 0:
               print(Red + "     Loading...")
          else:
               continue
elif n == 1:
     print(Green + "No have update version")
else:
     system.exit()