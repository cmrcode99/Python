canididate_name=input("Give me your name")
a_quiz_question=['True or False: 5000 meters = 5 kilometers.','(5 + 3)/2 * 10 = ?','Given the list [8, "Orbit", "Fuel Level", 45], what entry is at index 2?','Who was the first American woman in space?','What is the minimum crew size for the International Space Station (ISS)?',""]
correct_response=["true","40","fuel level","sally ride","3",""]
value= a_quiz_question[0]
answer_value= correct_response[0]
number=0
print("Canididate name: {}".format(canididate_name))
for turn in range(5):
  question=str(input(value).lower())
  print("Canididate Response: {}".format(question))
  print("Correct Answer: {}".format(answer_value))
  if question==answer_value:
    number= number+1
  value= a_quiz_question[1]
  answer_value= correct_response[1]
  del a_quiz_question[0]
  del correct_response[0]
  print("\n")
percent_correct=number/5 * 100
print(">>> Overall Grade: {}% ( {} out of 5 correct) <<<".format(percent_correct,number))
if number<4:
  print(">>> Status: Not Accepted <<<")
else:
  print(">>> Status: Accepted <<<")
  
 

  
  
  
