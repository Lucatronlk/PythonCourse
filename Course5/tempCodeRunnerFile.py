print("Alegeti una din urmatoarele: Piatra, Foarfeca, Hartie")
# user_guess = input()
# user_guess = user_guess.lower()
# user_guess = user_guess.strip()
# computer_guess = "piatra"

while True:
    user_guess = input()
    user_guess = user_guess.lower()
    user_guess = user_guess.strip()
    computer_guess = "piatra"
    if user_guess == "piatra":
        print("Egal")
        break
    elif user_guess == "foarfeca":
        print("Ai pierdut")
        break
    elif user_guess == "hartie":
        print("Ai castigat")
        break
    elif user_guess == "stop":
        print("Game over")
        break
    elif user_guess != "hartie" and user_guess != "foarfeca" and user_guess != "piatra":
        print("Please choose: Piatra, Foarfeca or Hartie")