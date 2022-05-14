cars = 100
space_in_a_car = 4
drivers = 30
passengers = 90
cars_not_driven = cars - drivers
cars_driven = drivers
carpool_capacity = cars_driven * space_in_a_car
average_passengers_per_car = passengers / cars_driven


# Number many cars are available
print("There are", cars, "cars available.")

# Number of drivers available
print("There are only", drivers, "drivers available.")

# Number of many empty cars
print("There will be", cars_not_driven, "empty cars today")

# Passenger capacity today
print("We can transport", carpool_capacity, "people today.")

# number of passengers to transport
print("We have", passengers, "to carpool today.")

# Average passengers per car
print("We need to put about", average_passengers_per_car, "in each car.")
