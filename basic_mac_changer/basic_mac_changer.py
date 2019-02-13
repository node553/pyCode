#!/usr/bin/env python

# allows us to execute system commands
import subprocess
# module that allows you to get arguments from the user and parse them
import optparse


# this function defines what argurment can be called and it parses the input
def get_arguments():
    # parser object that handles user input
    parser = optparse.OptionParser()
    # giving the object the interface argument it can expect from users
    parser.add_option("-i", "--interface", dest="interface", help="Interface to change its MAC Address")
    # giving the object the new MAC argument it can expect from users
    parser.add_option("-m", "--mac", dest="new_mac", help="New MAC Address")
    # telling the object to parse the arguments it gets from the user
    # returns all the info you get to wherever you call it
    (options, arguments) = parser.parse_args()
    # checking if they passed all the arguments needed
    if not options.interface:
        # code to handle if no interface argument is passed
        parser.error("[-] Please specify an interface, use --help or -h for more info")
    elif not options.new_mac:
         # code to handle if no MAC address argument is passed
        parser.error("[-] Please specify a MAC address, use --help or -h for more info")
    return options


# this function uses the subprocess.call() method to change the MAC addr
def change_mac_addr(interface, new_mac):
    # tells the user what the f**k is happening
    print("[+] Changing MAC Address on " + interface + " to " + new_mac)

    # system commands needed to change the MAC address
    # everytime there is a space you create a new item in the list
    subprocess.call(["ifconfig", interface, "down"])
    subprocess.call(["ifconfig", interface, "hw", "ether", new_mac])
    subprocess.call(["ifconfig", interface, "up"])



# setting options variable to the get arguments function
options = get_arguments()
# calling the change_mac_addr function and passing the variables from the object
change_mac_addr(options.interface, options.new_mac)
