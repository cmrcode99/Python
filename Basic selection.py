#!/bin/python3
user_entryy = input('Enter a word: ')

if len(user_entryy)> 5:
  print("{} is longer than 5 characters".format(user_entryy))
  # i) If the user's entry is longer than 5 characters, print "Your entry is longer than 5 characters!"
# Otherwise, print nothing.



# 1) If the number entered by the user is 100 or larger, print "Valid entry!"
# Otherwise, print, "Number too small."
num_entry = int(input('Enter a number larger than 100: '))

if num_entry > 100:
  print("Valid entry!")
else:
  print("Number too small.")


# 2) Prompt the user to enter a lowercase letter. Use the 'in' operator to check if the letter is a vowel
# (e.g. in the string 'aeiou'). If so, print, "___ is a vowel." Else, print, "___ is NOT a vowel."
user_letter = input('Enter a lowercase letter: ')
vowels = 'AaEeIiOoUu'
if user_letter in vowels:
  print("{} is a vowel".format(user_letter))
else:
  print("{} is NOT a vowel".format(user_letter)) 



# 3) What happens if the user enters a capital letter instead of lowercase?
# Refactor your code for problem 3 so that it works for both capital and lowercase vowels!
