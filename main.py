# This is the template code for the CNE335 Final Project
# Justin Ellis
# CNE 335 Fall

import Server

def print_program_info():
    # TODO - Change your name
    print("Server Automator v0.1 by Your Name")

# This is the entry point to our program
if __name__ == '__main__':
    print_program_info()
    #The server.Server("IP ADDRESS GOES HERE") in this case EC2 IP is 52.14.192.27
    #The IP address is passed as a string to the Server class in the server.py module
    ec2Server = Server.Server("52.26.15.148")
