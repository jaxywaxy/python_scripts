name = 'Jacqui Rennie'
age = 50 # not a like
height = 155 # centimeters
weight = 72 # lbs
eyes = 'blue'
teeth = 'white'
hair = 'blonde'
height_in_inches = height / 2.54
weight_in_lbs = weight * 2.2

print(f"Lets talk about {name}.")
print(f"She's {height} centimeters  or {round(height_in_inches)} inches tall")
print(f"She's {weight} kilos or {round(weight_in_lbs)} pounds heavy. ")
print(f"Actually, that's not too heavy.")
print(f"She's got {eyes} eyes and {hair} hair.")
print(f"Her teeth are usually {teeth} depending on the coffee.")

# print the total of  my details

total = age + height + weight
print(f"If I add {age}, {height}, and {weight} I get {total}.")
