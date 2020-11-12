correct_answer = "Tesla"
input_answer = input("Please guess the company of the electric car:\n")

def car_guess():
    
  if correct_answer == input_answer:
  	print("Correct")
  else:
  	car_guess()
 