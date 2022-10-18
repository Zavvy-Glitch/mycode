#!/usr/bin/python3

""" TLG Cohort D23 | CChea
    Conditional Practice - Testing Strings """


ipchk = input("Apply an IP Address: ")

if ipchk == "192.168.70.1":
    print(f"Looks like the IP address of the Gateway was set to: {ipchk}. This is not recommended!")
elif ipchk:
    print(f"Looks like the IP addres was set to: {ipchk}")
else:
    print("You did not provide an input.")
