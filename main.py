import os
import sys
sys.path.append(os.path.dirname(__file__))

import ConfigParser as cp
from os import path
import argparse
from transfer.base import Transfer
from walker import Walker

def main(file_path=None, all_sync=False):
    inifile = cp.SafeConfigParser()
    inifile.read(os.getcwd() + "/confing.ini")

    """ load config file """
    host = inifile.get("receiver", "host")
    port = inifile.get("receiver", "port")
    user = inifile.get("receiver", "user")
    passwd = inifile.get("receiver", "passwd")
    header_path = inifile.get("file", "header_path")

    transfer = Transfer("ftp")
    transfer.inst.connect(host, port, user, passwd)

    if all_sync:
        syncdir = inifile.get("all_sync", "syncdir")
        walker = Walker(syncdir)
        w = walker.start()
        while True:
            try:
                file_path = w.next()
                remote_path = file_path.replace(header_path, "")
                dirname = os.path.dirname(remote_path)
                filename = os.path.basename(remote_path)
                send(transfer.inst, dirname, filename, file_path)
            except StopIteration:
                return

    if file_path:
        remote_path = file_path.replace(header_path, "")
        if remote_path[0] != "/":
            remote_path = "/" + remote_path
        dirname = os.path.dirname(remote_path)
        filename = os.path.basename(remote_path)

        """ Connection with remote server """
        send(transfer.inst, dirname, filename, file_path)

def send(transfer, dirname, filename, file_path):
    # Need space on top of directory name.
    # But I don't know why this is required...
    transfer.mkdir(" "+dirname)
    transfer.send(dirname, filename, file_path)

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="FTP transfer")
    parser.add_argument(
            "-f", "--file", dest="file_path", default=None, help="file path")
    parser.add_argument(
            "-a", "--all", dest="all_sync", default=None, help="all sync")
    args = parser.parse_args()
    main(args.file_path, args.all_sync)

