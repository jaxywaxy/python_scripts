# this one is like scripts with argv
def print_two(*args):
    arg1, arg2 = args
    print(f"arg1: {arg1}, arg2: {arg2}")

# Print 2 args - different
def print_two_again(arg1, arg2):
    print(f"arg1: {arg1}")

# one argument
def print_one(arg1):
    print(f"arg1: {arg1}")

# this one takes no arguments
def print_none():
    print("I got nothing.")

print_two("Jacqui","rennie")
print_two_again("jacqui","rennie")
print_one("First!")
print_none()
