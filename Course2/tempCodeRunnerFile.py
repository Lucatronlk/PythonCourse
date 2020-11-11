input_answer = int(input("Please write the size of Motorbike's engine:\n"))      
def motorbike_tax(tax):
 
  if input_answer < 400: 
  	 print("The cost is 50 euro")
  elif input_answer > 400 and input_answer < 800: 
  	 print("The cost is 100 euro")
  elif input_answer > 800 and input_answer < 1200: 
  	 print("The cost is 150 euro")   
  elif input_answer > 1200 and input_answer < 1600: 
  	 print("The cost is 200 euro")     
  elif input_answer > 1600 and input_answer < 2000: 
  	 print("The cost is 400 euro")   
  elif input_answer > 2000 and input_answer < 2300: 
  	 print("The cost is 450 euro")


print(motorbike_tax(input_answer))           