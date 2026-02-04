#########List for datatypes############
my_list = [1, 2, 3, 4, 5, 6, 7]
print("Mylist:", my_list)

servers = ["192.168.1.1","192.168.1.2","192.168.1.3"]
print("server ips list:", servers)

## Add and Modified in a list of datatype (mutable) 
my_list[0] = 5                     ## modfied the value of this number array
my_list[4] = 10                    ## modfied the value of this number array
print("Modified Mylist:", my_list)

servers.append("192.168.1.4")     ## add new ip
print("Modified server ips list:", servers)


##########Tuple for datatypes########### (immutable: it mean, can't change existing)
my_tuple = (1, 2, 3, 4, 5, 6, 7)
print ("my tuple list:", my_tuple)
## for testing
my_tuple[2] = 6                        ## it will thorw error. so it mean it is immutable
print ("my tuple list:", my_tuple)


