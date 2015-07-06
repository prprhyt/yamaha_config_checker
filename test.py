
"""
from time import sleep
import checkconfigFnc

import telnetlib

HOST = "192.168.200.240"  # your server
user = "bty"             # your username
password = "*****"       # your password

tn = telnetlib.Telnet(HOST)

tn.read_until("Password:")
tn.write( "\n")
tn.read_until("> ")

tn.write("show config \n ")
sleep(1)
tn.write(" ")
sleep(1)
tn.write("exit \n")
str = tn.read_all()
print str
configlist =str.split("\r\n")
print configlist
confcount = len(configlist)

class confCls: pass

cnfg = confCls()
cnfg.conflist = configlist
cnfg.config=[]
"""
"""
for i in range(0,len(configlist)):
    cnfg.config[i] = configlist[i];


print cnfg.config
"""
from checkconfigClass import *

HOST = "192.168.200.240"  # your server
user = "bty"             # your username
password = "*****"       # your password

cnfg = Conf(user,HOST,password)
a=cnfg.conf_list
print a
b=cnfg.checkconfig('vlan-trunk')
print b

#print checkconfigFnc.checkconfig('vlan-trunk',cnfg.conflist)






