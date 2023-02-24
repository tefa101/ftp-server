from pyftpdlib.authorizers import DummyAuthorizer
from pyftpdlib.handlers import FTPHandler
from pyftpdlib.servers import FTPServer

#use any port higher than 1028 or run in root or adminstrator
PORT = 1211 

USER = 'stuckinreverse'
PASS = 1211



def start_ftp_server():
    # Instantiate a dummy authorizer for managing 'virtual' users
    authorizer = DummyAuthorizer()

    # Define a new user having full r/w permissions and a read-only anonymous user
    authorizer.add_user("user", "password", "/path/to/home", perm="elradfmwMT")
    authorizer.add_anonymous("/path/to/public")

    # Instantiate FTP handler class
    handler = FTPHandler
    handler.authorizer = authorizer

    # Define a customized banner (string returned when client connects)
    handler.banner = "Welcome to my FTP server"

    # Instantiate FTP server class and listen on 0.0.0.0:2121
    address = ("0.0.0.0", 2121)
    server = FTPServer(address, handler)

    # Set a limit for connections
    server.max_cons = 256
    server.max_cons_per_ip = 5

    # Start the FTP server
    server.serve_forever()


if __name__ == '__main__':
    start_ftp_server()
