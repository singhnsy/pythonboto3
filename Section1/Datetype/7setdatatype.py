#set datatype
my_sets = { 1, 2, 3, 4, 5, 6}
print("my sets:", my_sets)

my_sets.add(9)
print("my modified sets:", my_sets)

## remove spacific number from set list
my_sets.remove(5)
print("remvoe 5 number from sets:",my_sets)


########::Other Example::###########
server_ips = {"192.168.1.1", "192.168.1.2", "192.168.1.3"}
print("server_ips list:", server_ips)

## adding new ips in unorder position 
server_ips.add("192.168.1.4")
print("modified server_ips list:", server_ips)
 
 ## updating new ips
 #new_ips = ["192.168.1.5","192.168.1.6"]
 #server_ips.update(new_ips)
 #print("ADDing two more ips:", server_ips) 
