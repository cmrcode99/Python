date = "Monday 2019-03-18"
time = "10:05:34 AM"
average_astronaut_mass =	80.7
fuel_mass = 760000
ship_mass = 74842.31
fuel_level = "100%"
number_of_astronauts = int(input("How many astronauts were there?(1-7)"))
crew_status = input("Are you ready?(Ready or Not Ready)")
crew_mass =(number_of_astronauts*average_astronaut_mass)
total_ship_mass = (crew_mass + ship_mass + fuel_mass)

print("-------------------")
print("> LAUNCH CHECKLIST")
print("-------------------")
print("Date: {}\nTime: {}\n\n".format(date,time))
print("-------------------")
print("> SHIP INFO")
print("-------------------")
print("Crew: {}".format(number_of_astronauts))
print("Crew Status: {}".format(crew_status))
print("Fuel Level: {}\n\n".format(fuel_level))
print("-------------------")
print("> MASS DATA")
print("-------------------")
print("Crew: {}".format(crew_mass))
print("Fuel: {}".format(fuel_mass))
print("Spaceship: {}".format(ship_mass))
print("Total Mass: {}".format(total_ship_mass))


