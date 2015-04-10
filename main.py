# -*- coding: utf-8 -*-

import ConfigParser as cp
import os
from os import path
import argparse
from transfer.base import Transfer


def main(file_path=None):
    inifile = cp.SafeConfigParser()
    inifile.read(os.getcwd() + "/confing.ini")

    """ load config file """
    host = inifile.get("receiver", "host")
    port = inifile.get("receiver", "port")
    user = inifile.get("receiver", "user")
    passwd = inifile.get("receiver", "passwd")
    header_path = inifile.get("file", "header_path")

    if not os.path.exists(file_path):
        raise EOFError("No exist argumet file")
    remote_path = file_path.replace(header_path, "")
    print "remote: " + remote_path
    if remote_path[0] != "/":
        remote_path = "/" + remote_path
    dirname = os.path.dirname(remote_path)
    filename = os.path.basename(remote_path)

    """ Connection with remote server """
    print dirname
    print filename
    print file_path
    transfer = Transfer("ftp")
    transfer.inst.connect(host, port, user, passwd)
    transfer.inst.mkdir(dirname)
    transfer.inst.send(dirname, filename, file_path)

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="FTP transfer")
    parser.add_argument("-f", "--file", dest="file_path", help="file path")
    args = parser.parse_args()
    import sys
    sys.path.append(os.path.dirname(__file__))
    main(args.file_path)

