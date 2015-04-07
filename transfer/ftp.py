# -*- coding: utf-8 -*-


class FTP_:

    def __init__(self, file_name=""):
        self.file_name = file_name + ".ftp"
        self.ftp = None

    def welcome(self):
        print "ok!"

    def test_ftp(self, host, port, user, passwd):
        """ test module """
        from ftplib import FTP
        self.ftp = FTP()
        self.ftp.connect(host, port)
        self.ftp.login(user, passwd)
        f = open(self.file_name, "wb")
        f.write("test")
        f.close()
        f = open(self.file_name, "rb")
        command = "STOR "+self.file_name
        self.ftp.storbinary(command, f)
        self.ftp.close()

    def connect(self, host, port, user, passwd):
        from ftplib import FTP
        self.ftp = FTP()
        self.ftp.connect(host, port)
        self.ftp.login(user, passwd)

    def send(self, file_path):
        f = open(file_path, "rb")
        command = "STOR " + file_path
        self.ftp.storbinary(command, f)

    def close(self):
        self.ftp.close()

if __name__ == "__main__":
    import random
    strings = "abcdefghijklmnopqrstuvwxyz"
    b = FTP_(
        "".join([random.choice(strings) for x in xrange(10)]))
    b.test_ftp("127.0.0.1", 40001, "user", "passwd")
