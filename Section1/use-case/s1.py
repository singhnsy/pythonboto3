import os
folder = input("Please provide the list for directories name with space in between:").split() #Here split function is use to 
print(folder)
for i in folder:
    try:
        file = os.listdir(i)   # here .listdir() is function pf os module.
    except FileNotFoundError:  # here FileNotFoundError is an error which handling by except and print prodivded output.
        print("Please provide a valid dircectory name, look like this dir not exist:" + i)
        break
    except PermissionError:    # here PermissionError is an error which handling by except and print prodivded output. 
        print("No access to this folder:" + i)
        break
    print("==========list for the folder====" + i)
    for j in file:
        print(j)