from sys import argv

script, filename = argv

print(f"We're going to erase {filename}.")
print("If you dont want that, hit CTRL-C (^C).")
print("If you do want that, hit RETURN.")

input("?")

print("Opening the file ...")
target = open(filename, 'w')

print("Truncating the file. Goodbye!")
target.truncate()

print("Now I'm going to ask you for three lines.")

line1 = input("line 1: ")
line2 = input("line 2: ")
line3 = input("line 3: ")

print("I'm going to write these to the file.")

lines = [line1, line2, line3 ]
target.writelines('\n'.join(lines))


print("And finally, we close it.")
target.close()

#open the file - name from input
txt = open(filename)

#print file name
print(f"Here's your file {filename}:")

#read file
print(txt.read())
print()

#Close file
txt.close()
