#!/usr/bin/env python

import subprocess
import optparse
import re


def get_arguments():
    parser = optparse.OptionParser()
    parser.add_option("-i", "--interface", dest="interface", help="Interface to change its MAC Address")
    parser.add_option("-m", "--mac", dest="new_mac", help="New MAC Address")
    (options, arguments) = parser.parse_args()
    if not options.interface:
        parser.error("[-] Please specify an interface, use --help or -h for more info")
    elif not options.new_mac:
        parser.error("[-] Please specify a MAC address, use --help or -h for more info")
    return options


def change_mac_addr(interface, new_mac):
    print("[+] Changing MAC Address on " + interface + " to " + new_mac)

    subprocess.call(["sudo", "ifconfig", interface, "down"])
    subprocess.call(["sudo", "ifconfig", interface, "hw", "ether", new_mac])
    subprocess.call(["sudo", "ifconfig", interface, "up"])


def get_mac_addr(interface):
    ifconfig_res = subprocess.check_output(["ifconfig", interface])
    # getting mac addr using regular expressions
    mac_addr_res = re.search(r"\w\w:\w\w:\w\w:\w\w:\w\w:\w\w", ifconfig_res)

    if mac_addr_res:
        return mac_addr_res.group(0)
    else:
        print("[-] Could not read MAC address")


options = get_arguments()
current_mac = get_mac_addr(options.interface)
print("Current MAC address = " + str(current_mac))
change_mac_addr(options.interface, options.new_mac)

current_mac = get_mac_addr(options.interface)
if current_mac == options.new_mac:
    print("[+] MAC was changed to: " + current_mac)
else:
    print("[-] MAC address did not get changed.")
