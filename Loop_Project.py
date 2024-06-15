date = "Monday 2019-03-18"
time = "10:05:34 AM"
average_astronaut_mass =	80.7
ship_mass = 74842.31

fuel_level = float(input("Enter a fuel percentage"))

place_holder_1= 1

if fuel_level < 90:
  place_holder_1 = 0

while place_holder_1 == 0  :
  refuel_option = input("Would you like to refuel (Yes/No)").lower()
  if refuel_option == "yes":
    fuel_level = 100
  if fuel_level == 100:
    place_holder_1= 1
  else:
    place_holder_1= 5
 
  
 
fuel_mass = 760000 * fuel_level/100

while place_holder_1 == 1:
  number_of_astronauts = int(input("How many astronauts were there?(1-7)"))
  if 0 < number_of_astronauts < 8:
    place_holder_1 = place_holder_1 + 1

if place_holder_1 == 2:
  place_holder_1 = 1
  
if place_holder_1 == 1:
  crew_status = input("Are you ready?(Ready or Not Ready)").lower()
if place_holder_1 == 1:
  crew_mass =(number_of_astronauts*average_astronaut_mass)
if place_holder_1 == 1:
  total_ship_mass = (crew_mass + ship_mass + fuel_mass)
while place_holder_1 == 1:
  if crew_status == "ready":
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
  else:
    print("This ship will not sail")
  place_holder_1 = place_holder_1 + 1

if place_holder_1 == 5:
  print("This ship will not sail")


