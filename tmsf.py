import pyfiglet
import os
os.system("clear")
os.system("echo    ")
os.system("echo  && echo && echo ")
print ("                                                     ")
from pyfiglet import Figlet
custom_fig = Figlet(font='graffiti')
print(custom_fig.renderText("    tmsf  "))
os.system("sleep 2.5 ")
print ("               |t|m|s|f|     ")
print ("                                                      ")
print (" (0)- install basic packages for this program ")
print (" (1)- install metasploit-framework in termux ")
print (" (2)- start metasploit-framework ")
print (" (3)- exit from the program ")
os.system("sleep 0.5")
print ("                                                     ")

choice = int(input("      enter your choice: "))
if choice == 0:
   os.system("sleep 0.2 && clear")
   os.system("apt-get upgrade && pkg update && apt-get upgrade && pkg upgrade && sleep 5  && clear ")
   os.system(" apt-get clean && dpkg --configure -a && sleep 2.5 && clear ")
   os.system(" apt-get install python python2 wget termimage curl -y ")
   os.system(" apt-get install termimage -y ")
   os.system ("sleep 3.5 ")
   os.system("clear ")
   os.system (" echo          ")
   print ("echo all basic packages for this program is installed ")
   os.system(" sleep 3.5")  
   os.system("echo          ")
elif choice == 1:
   os.system("clear")
   os.system("apt-get update && apt-get upgrade -y && clear ")
   os.system("pkg install wget curl openssh git -y && apt-get install wget curl openssh git -y ")
   os.system("apt install ncurses-utils && pkg install ncurses-utils ")
   os.system("wget https://raw.githubusercontent.com/gushmazuko/metasploit_in_termux/master/metasploit.sh ")
   os.system("chmod +x metasploit.sh && bash metasploit.sh ")
   
elif choice ==2:
   os.system("clear")
   os.system("chmod +x postgresql_ctl.sh ")
   os.system("./postgresql_ctl.sh start ")
   os.system("sleep 3")
   os.system("clear")
   os.system("msfconsole")

elif choice == 3:
   print (" you are selected to exit from this program")
   os.system("sleep 3.5")
   os.system("clear")
   os.system(" echo thanks for using this program ")
   os.system("sleep 2.5")
   os.system("echo you are now exited from this program ")
   os.system("sleep 1.5")
   os.system("clear")
else :
   os.system("clear")
   print (" you are choosed wrong choice no: ")
   os.system("sleep 3.5")
   print (" or you choosed options that is not available in this program ")
   os.system("sleep 4")
   print (" so by default program is exiting ...")
   os.system(" sleep 3.5")
   print (" you are now sucessfully exited from this program ")
   os.system(" sleep 3")
   os.system("clear")   