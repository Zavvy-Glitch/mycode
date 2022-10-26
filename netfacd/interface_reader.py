#!/usr/bin/python3

import netifaces

# print(netifaces.interfaces())

def main():
    """Iterates over network interfaces to find IP and MAC """

    for i in netifaces.interfaces():
        print('\n**************Details of Interface - ' + i + ' *********************')
        try:
            print('MAC: ', end='')
            print(netifaces.ifaddresses(i)[netifaces.AF_LINK][0]['addr'])
            print('IP: ', end='')
            print(netifaces.ifaddresses(i)[netifaces.AF_INET][0]['addr'])
        except:
            print("unable to reach, please check your code")

def filterIP():
    """ Iterates over network interface and displays IP based on device name """
    for i in netifaces.interfaces():
        device = input(""" 
Please choose a device:
    - lo
    - ens3
    - docker0
---> """)
        if i == device:
            print(f"{device} IP: ", netifaces.ifaddresses(device)[netifaces.AF_INET][0]['addr'])
            break

def filterMAC():
    """ Iterates over network interface and displays MAC based on device name """
    for i in netifaces.interfaces():
        device = input(""" 
Please choose a device:
    - lo
    - ens3
    - docker0 
---> """)
        if i == device:
            print(f"{device} MAC: ", netifaces.ifaddresses(device)[netifaces.AF_LINK][0]['addr'])
            break
