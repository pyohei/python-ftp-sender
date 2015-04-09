# -*- coding: utf-8 -*-


class Transfer:

    def __init__(self, connection_str):
        self.inst = None
        self.__connet(connection_str)

    def __connet(self, connection_str):
        defs = {
            "ftp": self.__ftp
            }
        self.inst = defs[connection_str]()

    def __ftp(self):
        from ftp import FTP_
        return FTP_()

if __name__ == "__main__":
    b = Transfer("ftp")
    b.inst.welcome()
    b.inst.test_ftp("127.0.0.1", 40001, "user", "passwd")
