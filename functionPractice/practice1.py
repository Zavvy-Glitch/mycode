#!/usr/bin/python3

""" Docstring """

import crayons


def commandPush(dataSet):
    
    for ip in dataSet.keys():
        print(f"{crayons.blue('Handshaking')} . .. ... connecting with {ip}")

        for mycmds in dataSet[ip]:
            print(f"Attempting to send command ---> {mycmds}")
    
    return None


def ipPush(i):
    print(f"Connecting to {i}. ..")

    print("REBOOTING NOW!")


def main():
    """ Set of code that will execute at runtime """

    # Dictionary that will be used in for loop iteration
    dataSet  = {"10.1.0.1":["interface eth1/2", "no shutdown"], "10.2.0.1":
    ["interface eth1/1", "shutdown"], "10.3.0.1":["interface eth1/5", "no shutdown"]}

    print(f"Welcome to the {crayons.yellow('Network')} device command pusher")

    print("\nData set found\n")
    
    # When this runs it will hoist the data set to to function of commandPush()
    commandPush(dataSet)

    for i in dataSet.keys():
        ipPush(i)

main()
