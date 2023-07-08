#writing a file
file=open("newfile.txt","w")
file.write("The key function for working with files in Python is the open() function.\nThe open() function takes two parameters; filename, and mode.\nThere are four different methods (modes) for opening a file:\nr - Read - Default value. Opens a file for reading, error if the file does not exist\na - Append - Opens a file for appending, creates the file if it does not exist\nw - Write - Opens a file for writing, creates the file if it does not exist\nx - Create - Creates the specified file, returns an error if the file exists")
file.close()
print("file created sucessfully")
#reading a file
file=open("newfile.txt","r")
re=file.read()
print("\n\t\t\t\twe are reading a file\n")
print(re)
file.close()