import re       ## re is powerfull tool for matching patterns in strng

#Reguler expresion to capture with 'Warning' or 'Error'
pattern = r"(WARNING|ERROR)"
# File path to the log file (example)
##log_file_path = "/var/log/messages"  
log_file_path = ".\\java_error_in_pycharm_24512.txt.log"
#Open and read the log file
with open(log_file_path, "r") as file:
    for line in file:
        # Search for the lines containing 'Warning' or 'Error'
        if re.search(pattern, line):
            print(line.strip())   # Print matching lines without extra spaces.

pattern1 = r"(error)"
log_file_path1 = ".\\java_error_in_pycharm_24512.txt.log"
with open(log_file_path1, "r") as file:
    for line1 in file:
        if re.search(pattern1, line1):
            print(line1.strip())
