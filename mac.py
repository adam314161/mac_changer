#!/usr/bin/env python

import subprocess
import optparse
import re
import codecs

def get_arguments():
    parser = optparse.OptionParser()

    parser.add_option("-i", "--interface", dest="interface", help="to change the mac")
    parser.add_option("-m", "--mac", dest="new_mac", help="new mac")
    (options, arguments) = parser.parse_args()
    if not options.interface:
        parser.error("[-] please specify an interface, use --help for info.")
    elif not options.new_mac:
        parser.error("[-] please specify a mac address, use --help for info")
    return options

def change_mac(interface, new_mac):
    print ("[+] new mac for " + interface + " to " + new_mac)

    subprocess.call(["ifconfig", interface, "down"])
    subprocess.call(["ifconfig", interface, "hw", "ether", new_mac])
    subprocess.call(["ifconfig", interface, "up"])


options = get_arguments()

# change_mac(options.interface, options.new_mac)

ifconfig_result = subprocess.check_output(["ifconfig", options.interface])
print (ifconfig_result)

mac_result = re.search(r"\w\w:\w\w:\w\w:\w\w:\w\w:\w\w", codecs.decode(ifconfig_result, "utf-8"))

if mac_result:
    print (mac_result.group(0))
else:
    print("[-] couldn't find mac address")
