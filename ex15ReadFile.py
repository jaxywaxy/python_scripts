from sys import argv

#argument values scriptname and filename from prompt
script,  filename = argv

#open the file - name from input
txt = open(filename)

#print file name
print(f"Here's your file {filename}:")

#read file
print(txt.read())

#Close file
txt.close()

#prompt for file name again
print("Type the filename again:")
file_again = input("> ")

#open file and read again
txt_again = open(file_again)
print(txt_again.read())

# Close file
txt_again.close()
