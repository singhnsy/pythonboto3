import os

#Get the current working directory 
current_directory = os.getcwd()
print(f"Current working directioy: {current_directory}")

#list of the file and directories
files =  os.listdir(".")
print(f"Files in the current dicrectory: {files}")