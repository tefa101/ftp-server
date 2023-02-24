import ftplib

HOST = 'enter a hostttt'
port = 1211



def connect_to_ftp():
    ftp = ftplib.FTP()
    ftp.connect('your_ftp_server_address', 2121) # Replace 'your_ftp_server_address' with the actual address of your FTP server

    ftp.login(user='user', passwd='password') # Replace 'user' and 'password' with the actual username and password for your FTP server

    # Once connected, you can interact with the server using various FTP commands
    ftp.cwd('/path/to/remote/directory') # Change to the remote directory where you want to upload or download files

    # # Example: Upload a file to the server
    # with open('local_file.txt', 'rb') as f:
    #     ftp.storbinary('STOR remote_file.txt', f)

    # Example: Download a file from the server
    with open('local_file.txt', 'wb') as f:
        ftp.retrbinary('RETR remote_file.txt', f.write)

    ftp.quit() # Close the FTP connection

if __name__ == '__main__':
    connect_to_ftp()