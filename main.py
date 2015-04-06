# -*- coding: utf-8 -*-

import ConfigParser as cp
import os

inifile = cp.SafeConfigParser()
inifile.read(os.getcwd() + "/confing.ini")

print inifile.get("sender", "basedir")
print inifile.get("receiver", "basedir")

