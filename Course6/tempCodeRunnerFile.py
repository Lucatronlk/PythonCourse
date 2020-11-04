CARS = ["audi","bmw","hyundai","dacia"]
STATUS = False	
while STATUS == False:
  USER_INPUT = input("Enter a car type: ")
  if USER_INPUT in CARS:
    print("You guessed the car!")
    STATUS=True
  else:
    print("You have not guessed the car!")