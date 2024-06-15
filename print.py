word_needed= input("Enter a word")
adx= len(word_needed)
print("The word '{}' contains {} characters \n \n".format(word_needed,adx))

rectangle_length= float(input("Gimme a Rectangle Length"))
rectangle_width= float(input("Gimme a width"))

rectangle_area= rectangle_length*rectangle_width
print("This rectangle has and area of {} \n \n".format(rectangle_area))

MDD= float(input("How many miles did you drive?"))
GUU= float(input("How many gallons did you use?"))
MPG= MDD/GUU
print("Your car got {} miles per gallon".format(MPG))
