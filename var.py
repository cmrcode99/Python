#!/bin/python3
# 1. Declare and assign your first 4 variables here:
ship_name = 'Determination'
Ship_Speed_Mph= 17500
Distance_To_Mars_Km= 225000000
Miles_Per_Kilometer= 0.621

# 2. Create and assign a miles to Mars variable here:
Miles_To_Mars= float(Distance_To_Mars_Km*Miles_Per_Kilometer)


# 3 & 4. Calculate and store the hours it takes to get to Mars and the days to Mars:
Hours_To_Mars=(Miles_To_Mars/Ship_Speed_Mph)
Days_To_Mars= (Hours_To_Mars/24)




# 5. Print the sentence, "_____ will take ___ days to reach Mars." Fill in the blanks with the spaceship name and the calculated time.
print("{} wil take {} days to get here".format(ship_name,Days_To_Mars))
