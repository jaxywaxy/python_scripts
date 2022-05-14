types_of_people = 10
x = f"There are {types_of_people} types of people."


binary = "binary"
do_not = "don't"
y = f"Those who know {binary} and those who {do_not}." #string inside a string

print(x) #print line x
print(y)

print(f"I said: {x}") # print a string inside of a string
print(f"I also said: '{y}'") # print another string inside a string

hilarious = False
joke_evaluation = "Isn't that joke so funny?! {}"

print(joke_evaluation.format(hilarious)) #evaluate joke and print a string inside a string

# print strings
w = "This is the left side of..."
e = "a string with a right side."

print(w + e)
