#!/usr/bin/python3
""" TLG Cohort D23 | CChea
    built in methods for lists """


proto = ["ssh", "http", "https"]
protoa = ["ssh", "http", "https"]
print(protoa)
proto.append("dns") # this line will add "dns" to the end of our list
protoa.append("dns") # this line will add "dns" to the end of our list
print(proto)
proto2 = [ 22, 80, 443, 53 ] # a list of common ports
proto.extend(proto2) # pass proto2 as an argument to the extend method
print(proto)
protoa.append(proto2) # pass proto2 as an argument to the append method
print(protoa)



