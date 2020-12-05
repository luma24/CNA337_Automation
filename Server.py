import os

class Server:
    """ Server class for representing and manipulating servers. """

    def __init__(self, server_ip):
        # TODO -
        self.server_ip = server_ip

    def ping(self):
        # TODO - Use os module to ping the server
        response = os.system("ping -n 4 " +self.server_ip)
        return self.server_ip
    
# NEXT,   
# Automate SSH:
# Connect to my AWS Instance using my SSH key
# Run Update and Upgrade commands in the package manager
# Disconnect from server


# This link helped me with the "Bad Authentication type; allowed types['pubilickey'] Error:
# https://stackoverflow.com/questions/2224066/how-to-convert-ssh-keypairs-generated-using-puttygen-windows-into-key-pairs-us

## This website showing how to use paramiko:
# https://mainlydata.kubadev.com/python/using-paramiko-to-control-an-ec2-instance/

import paramiko
# create client ssh object so we can use it to connect to the server
ssh = paramiko.SSHClient()
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())  # THE MISSING KEY WILL BE ADDED

ssh.connect('3.17.16.187', port=22, username='ubuntu', password='', key_filename='Luma-key.Exported')

stdin, stdout, stderr = ssh.exec_command('''sudo apt-get update
                                         sudo apt-get upgrade -y
                                         ''')  # site to force the upgrade: https://itsfoss.com/update-ubuntu/
stdin.flush()
data = stdout.read().splitlines()
for line in data:
    print(line)

ssh.close()

# I worked with Hasan.
# Zak helped me to troubleshoot the error!Thanks!
