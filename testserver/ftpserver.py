# -*- coding: utf-8 -*-

import pyftpdlib.authorizers
import pyftpdlib.handlers
import pyftpdlib.servers
import os

my_dir = os.getcwd()

authorizer = pyftpdlib.authorizers.DummyAuthorizer()
authorizer.add_user("user", "passwd", my_dir, perm="elreadfmw")

handler = pyftpdlib.handlers.FTPHandler
handler.authorizer = authorizer

server = pyftpdlib.servers.FTPServer(("127.0.0.1", 40001), handler)
server.serve_forever()
