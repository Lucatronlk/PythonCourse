list_num = []
i = 0

while i < 10:
    list_num.append(i)
    i += 1

import random

# print ("Ghiceste numarul intre 0 si 10 ")
# guess_num = input()
# number = random.choice(list_num)

# guess_num = int(guess_num)

while True:
    guess_num = input("Give a number between 1 and 10: ")
    number = random.choice(list_num)
    if guess_num == number:
        print("Felicitari ai ghicit numarul")
        break
    elif guess_num == "STOP":
        print("GAME OVER")
        break
    elif guess_num != number:
        print(" Din pacate nu ai ghicit numberu " + "Numarul a fost " + str(number))
