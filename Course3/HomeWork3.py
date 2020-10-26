import random
from random import randint

# 1. De cate ori apare numarul 8 in lista?

list = [1, 10, 9, 8, 8, 7, 8, 11, 2, 7, 89, 8, 90,24, 8, 5] 

my_list = {i:list.count(i) for i in list}
print(my_list)

#Generati primele 50 de numere in ordine descrescatoare

list_2 = []
i = 0
while i < 50:
    i += 1
    list_2.append(i)
    
list_2.sort(reverse=True)
    
print(list_2)

#3 Creati o noua lista care sa fie ca cea de mai sus dar fara litera a 

list_3=["a", "b", "c", "a", "d", "e", "b", "a"] 

final_list = list(dict.fromkeys(list_3))
final_list.remove("a")

print(final_list)


#4 Generati toate numerele intre 123 si 231

list_4=[]
i = 122

while i < 231:
    i+=1
    list_4.append(i)

print(list_4)   


#5 Generati toate numerele pare intre 500 si 560

list_5=[]
i = 499

while i < 560:
    i+=1
    if i % 2 == 0:
        list_5.append(i)

print(list_5)   


#6 Generati toate numerele impare in ordine descrescatoare intre 999 si 901 

list_6=[]
i = 900

while i < 999:
    i += 1
    if i % 2 == 1:
        list_6.append(i)


list_6.sort(reverse=True)
print(list_6)

#7 Jucati o tura de piatra, foarfece, hartie cu user-ul

list_rps = ['Piatra', 'Foarfeca', 'Hartie']
print("Alege Piatra, Foarfeca sau Hartie")
user_rps = str(input())

computer = list_rps[randint(0, 2)]

#set player to False
player = False

while player == False:
#set player to True
    player = user_rps
    if player == computer:
        print("Egal")
    elif player == "Piatra":
        if computer == "Hartie":
            print("Ai pierdut!", computer, "acopera", player)
        else:
            print("Ai castigat!", player, "sfarama", computer)
    elif player == "Hartie":
        if computer == "Foarfeca":
            print("Ai pierdut!", computer, "taie", player)
        else:
            print("Ai castigat!", player, "acopera", computer)
    elif player == "Foarfeca":
        if computer == "Piatra":
            print("Ai pierdut...", computer, "sfarama", player)
        else:
            print("Ai castigat!", player, "cut", computer)
    else:
        print("Nu ai facut o alegera corecta, Alege una din urmatoarele variante: Piatra, Foarfeca, Hartie!")
    
    #player was set to True, but we want it to be False so the loop continues
    player = False
    computer = list_rps[randint(0,2)]

#8 Cereti user-ului sa introduca un numar intre 1 si 10. Daca nu respecta cerinta, printati un mesaj de eroare

print ( "Introdu un numar intre 1 si 10 " )
user_int = input()

if user_int.isdigit and user_int <= 10():
        print (user_int)
else:
        print ( "Numarul nu este intre 1 si 10" ) 
    

#9  Puneti prefixul "oras" la fiecare element din lista de mai sus

list_oras = ["Timisoara", "Oradea", "Bucuresti", "Brasov", "Constanta", "Cluj"]

append_prex = "Oras "

pre_res = [append_prex + sub for sub in list_oras]

print(str(pre_res))

#10 Adunati toate numerele din lista de mai sus

list_sum = [10, 99, 876, 23, -40, 78, -2000]

print(sum(list_sum))


#11 Intrebati-l pe user parola si ziceti daca e slaba, moderata sau puternica. Daca e sub 10 caractere e slaba, iar peste 20 puternica


print ('Create a new password')
print ()
password = str(input())

def password(user_password):

    if len(password) < 10:
        print ("The password is wery week, you can consider changing it ")
    elif len(password) < 20:
        print ("The Password is moderate.....")
    elif len(password) >= 20:
        print("Your password is strong, Good job")