#1   Are the following if statements True or False:
#    a. if True and False: --> FALSE
if True and False:
    print("it is false'")
else:
    print('we are in else')

#    b. if False or True: --> TRUE
if False or True: 
    print('this will always be true')
else:
    print('nu o sa ajunga niciodata')


#    c. if 10 >= 10 and 67 > 66: --> TRUE

x = 10 >= 10 and 67 > 66 
print('ex c = ')
print(x)

#    d. if 10 < 10 and 10 >= 9: --> FALSE
d = 10 < 10 and 10 >= 9
print(d)

#    e. if -1 < -2 or -2 > -1: --> FALSE

e = -1 < -2 or -2 > -1
print(e)

#    f. if True or False and True: --> TRUE

f = True or False and True
print(f)

#    g. if True and False or False and True: --> FALSE

g = True and False or False and True
print(g)

#    h. if not True and not False: --> FALSE

h = not True and not False
print(h)

#    i. if not True or True: --> TRUE
 
i = not True or True
print(i)

#    j. if False and not False: --> FALSE

j = False and not False
print(j)

#2. What values should x,y have so the following if statements are True? What about False?
#    a. if x > 6 and x < 12:  -->  TRUE: 7 > 6 and 7 < 12   | FALSE: 13 > 6 and 13 < 12

x = 7
a = x > 6 and x < 12
print(a)

x = 13
a = x > 6 and x < 12
print(a)

#    b. if x > 10 or y > 10:  -->  TRUE: 11 > 10 or 9 > 10  | FALSE: 9 > 10 or 8 > 10

x=11
y=9
b = x > 10 or y > 10
print(b)

x=9
y=8
b = x > 10 or y > 10
print(b)

#    c. if x < 9 or True:     -->  TRUE: 9 < 9 or True      | FALSE: Cannot be false because one value is true 

x = 9 
c = x < 9 or True
print(c)

#    d. if y > 99 and False:  -->  TRUE: Cannot be true     | FALSE: 99 > 99 and False 

y = 99
d = y > 99 and False
print(d)

#    e. if x > 10 and x < 10: -->  TRUE: cannot be true | FALSE:  9 > 10 and 9 < 10

x = 9
e = x > 10 and x < 10
print(e)

#    f. if not x:             -->  TRUE not False           | FALSE: not True

x = False
f = not x
print(f)

x = True
f = not x
print(f)

#    g. if x > 10 or x < 10:  -->  TRUE 11 > 10 or 10 < 10  | FALSE 10 > 10 or 10 < 10

x = 11
g = x > 10 or x < 10
print(g)

x = 10
g = x > 10 or x < 10
print(g)


#    h. if x > 12 and x < 18 or y > 4 and not y < 89:  -->    TRUE:  13 > 12 and 13 < 18 or 90 > 4 and not 90 < 89 | FALSE: 11 > 12 and 11 < 18 or 3 > 4 and 3 < 89


x = 13
y = 90
h = x > 12 and x < 18 or y > 4 and not y < 89
print(h)


x = 11
y = 3
h = x > 12 and x < 18 or y > 4 and not y < 89
print(h)


#3 Exercises with lists
list1 = [1, 3, 45, -7, 89, 1, 12, 3, 3, 1]
list2 = ["a", "cd", "b", "b", "f", "oj", "Zz"]
list3 = [1, 2, "a", 34, "bgh", "#"]
    
#    a. eliminate all elements from list3

list3.clear()
print(list3)

#    b. eliminate all 3 from list1

#list1.remove(3)
while 3 in list1:
    list1.remove(3)
print(list1)

# #    c. sort list1 from the biggest number to the lowest

list1.sort(reverse=True)
print(list1)

# #    d. sort list2 without "Zz"
list2.pop()
list2.sort()
print(list2)

# #    e. make list3 in the recverse order

list3.reverse()
print(list3)
#    f. eliminate last 3 elements from list 2, last element from list3 and last 2 elements from list1

n = 3

res = list2[: len(list2) - n ]

print(res)

list3.pop()

m = 2

res_2 = list1[: len(list1) - m ]
print(res_2)



i = 3 
print(list2)
while i > 0:
    list2.pop()
    i -=1
print(list2)

list1 = list[:-2] # scoate ultimele 3


#g how many b values are in list 

print(list2.count('b'))

#4. Exercises with dictionaries
dict1 = {'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 'A'}
#    a. remove last element

dict1.popitem()
print(dict1)

#    b. print all keys for the values above 2

for key, value in dict1.items():
    if value > 2:
        print(key)

#    c. remove all keys for the values above 2

keys_to_be_removed = []
for key, value in dict1.items():
    if value > 2:
        keys_to_be_removed.append(key)

for key in keys_to_be_removed:
    dict1.pop(key)
print(dict1)    

dict1 = {key : val for key, val in dict1.items() if not (isinstance(val, int) and (val > 2))}
print(dict1)

#    d. print all the values remaining

print(dict1.values())
#    e. remove all remaining elements from dict


dict1.clear()

print(dict1)


# 5. Make a "piatra, foarfece, hartie" game. 
#    If the user types 'stop', even with whitespaces or some uppercase letters, the game stops.
#    The user needs to input "piatra", "foarfece" or "hartie". 
#    If he writes something else, inform him on the rules of the game.
#    Accept the user's input even if it has whitespaces or some letters are uppercase.

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
        



# 6. Make a game in which the user has to guess a number between 100 and 199.
#    If the user types 'stop', even with whitespaces or some uppercase letters, the game stops.
#    If the user's number is not between 100 and 199, inform him.
#    If the user does not enter a number, inform him.



import random 
list_num = []
i = 100

while i <= 199:
    list_num.append(i)
    i+=1

print(list_num)
print("Choose a number between 100-109")


while True: 
    guess_num = input("Give a number between 100 and 199: ")
    guess_num = guess_num.strip()
    guess_num = guess_num.upper()
    number = random.choice(list_num)
    if guess_num == number:
        print ("Felicitari ai ghicit numarul")
        break
    elif guess_num == "STOP":
        print("GAME OVER")
        break
    elif int(guess_num) < 100 or int(guess_num) > 199:
        print("Numarul ales nu este intre 100 si 199")
    elif guess_num != number:
        print (" Din pacate nu ai ghicit numberu " + "Numarul a fost " + str(number))



