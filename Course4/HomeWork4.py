import random
import sys

#1: Scrieti un program in python care aduna toate numerele pe care le da user-ul prin terminal

args = sys.argv
print(args) 

numbers = args[1:]
print(numbers)

sum = 0 
for number in numbers:
    sum += int(number)

print(sum)    



#2 Scrieti un program in care user-ul trebuie sa introduca un numar intre 50 si 100. 
# Daca introduce alt numar, printati "Your number is below 50" sau "Your number is above 100". 
# Daca introduce litere, printati "You should enter a number"

print("Va rog introduceti un nr intre 50 si 100")
user_numb = input()

if user_numb < 50:
    print("Your number is bellow 50")
elif user_numb > 100:
    print ("Your number is above 100")    
elif user_numb.isalpha():
    print("You should enter a number")



# 3: Intr-un fisier definiti o functie care verifica daca un numar e par sau impar. 
# In alt fisier, verificati un numar dat de user daca e sau nu par folosind functia definita in celalalt fisier.





#Exercitiu 4: Creati un joc in care user-ul trebuie sa ghiceasca un numar intre 1 si 10. 
# La fiecare input al user-ului ziceti numarul ales de calculator (folositi random.choice). Jocul se opreste doar cand user-ul tasteaza "STOP"

list_num = []
i = 0

while i < 10:
    list_num.append(i)
    i+=1


import random
print ("Ghiceste numarul intre 0 si 10 ")
guess_num = input()
number = random.choice(list_num)

#guess_num = int(guess_num)


while True:
    if guess_num == number:
        print ("Felicitari ai ghicit numarul")
        break
    elif guess_num != number:
        print (" Din pacate nu ai ghicit numberu " + "Numarul a fost " + str(number))
        break
    elif guess_num == "STOP":
        print("GAME OVER")
        
    