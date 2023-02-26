import ftplib

HOST = 'X.X.X.X'
port = 1211
username = 'stuckinreverse'
password = '1211'



def connect_to_ftp():
    ftp = ftplib.FTP()
    ftp.connect('192.168.1.12', 1211) # Replace 'your_ftp_server_address' with the actual address of your FTP server

    ftp.login(user=username, passwd=password) # Replace 'user' and 'password' with the actual username and password for your FTP server

    # Once connected, you can interact with the server using various FTP commands
    ftp.cwd('/path/to/remote/directory') # Change to the remote directory where you want to upload or download files

    # # Example: Upload a file to the server
    # with open('local_file.txt', 'rb') as f:
    #     ftp.storbinary('STOR remote_file.txt', f)

    # Example: Download a file from the server
    with open('wget.cmd', 'wb') as f:
        ftp.retrbinary('RETR wget.cmd', f.write)

    ftp.quit() # Close the FTP connection

if __name__ == '__main__':
    connect_to_ftp()