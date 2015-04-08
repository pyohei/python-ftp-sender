# -*- coding: utf-8 -*-

import ConfigParser as cp
import os
import argparse

inifile = cp.SafeConfigParser()
inifile.read(os.getcwd() + "/confing.ini")

print inifile.get("sender", "basedir")
print inifile.get("receiver", "basedir")

def main(file_path=None):
    print "main"

if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description="FTP transfer")
    parser.add_argument("-f", "--file",
        dest="file_path", help="file path")
    args = parser.parse_args()
    main(args.file_path)

