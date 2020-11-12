import random

list_num = []
i = 100

while i <= 199:
    list_num.append(i)
    i += 1

print(list_num)
print("Choose a number between 100-109")

while True:
    guess_num = input("Give a number between 100 and 199: ")
    guess_num = guess_num.strip()
    guess_num = guess_num.upper()
    number = random.choice(list_num)
    if guess_num == number:
        print("Felicitari ai ghicit numarul")
        break
    elif guess_num == "STOP":
        print("GAME OVER")
        break
    elif int(guess_num) < 100 or int(guess_num) > 199:
        print("Numarul ales nu este intre 100 si 199")
    elif guess_num != number:
        print(" Din pacate nu ai ghicit numberu " + "Numarul a fost " + str(number))
    else:
        print('Va rog alegeti un numar')
