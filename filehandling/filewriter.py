name = "Arlene" # Modify by writing your name here.
file = open("newfile1.txt", 'w')
file.write(f"Hello, {name}!\n")
file.write("Isn't this amazing?\n")
file.write("that we can create and write on text files\n")
file.write("using Python.")
file.close()

#Modifcation of the program
file = open("newfile2.txt", 'w')
file.write("This message was created using Python!")
file.close()