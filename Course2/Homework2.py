from math import gcd
import operator

# 1. Generate & print the list of the first 500 odd numbers

# list=[]
# i = 1
# while i <= 500:
#     list.append(i)
#     i += 1
#     n = 2 * i - 1
#     print(n)
#     i = i + 1 
# print (list)

list = []
i = 0
while len(list) < 500:
    i += 1
    if i % 2 == 1:
        list.append(i)
print(list)
print(len(list))

# 2.Generate & print the first 30 prime numbers

list_odd = []
i = 0
while i <= 30:
    list_odd.append(i)
    i += 1

start = 0
end = 30
for i in range(start, end):
    if i > 1:
        for j in range(2, i):
            if (i % j) == 0:
                break

        else:
            print(i)

# 3. Create a game in which the user must guess an animal. He has 20 tries

animal = "Leu"
print("Te rog sa ghicesti animalul")
user_animal = input()

turns = 20

while turns > 0:
    if user_animal == animal:
        print("Ai ghicit Animalul")
        break
    else:
        print("Nu ai ghicit")
        print("Incearca din nou")
        user_animal = input()
        turns -= 1

if turns == 0:
    print("Game Over")

# 4. Create a game in which the user must guess the type of a car. The program stops only when the user guesses

car = "Volvo"
print("Te rog sa ghicesti marca de masina")
user_car = input()

while True:
    if car == user_car:
        print("Raspuns Corect")
        break
    else:
        print("Raspuns gresit, Te rog mai incearca")
        user_car = input()

# 5. Create a function which takes 2 ints and returns the greatest common divisor & the lowest common multiple. Make 5 tests for the function

print("Primul numar")
user_int1 = input()
print("Al doilea numar")
user_int2 = input()


def lcm_gcd(user_int1, user_int2):
    def gcd(user_int1, user_int2):
        while user_int2 > 0:
            user_int1, user_int2 = user_int2, user_int1 % user_int2
            return user_int1


def lcm(user_int1, user_int2):
    return user_int1 * user_int2 / gcd(user_int1, user_int2)


print(gcd(user_int1, user_int2))
print(lcm(user_int1, user_int2))

# 6. Make a dictionary with 10 key/values. The keys represent the name of a product & the value the price of the product.
# Create a function which returns the name of the product with the lowest price above 100.


dict = {'monitor': 2700, 'laptop': 5000, 'mouse': 100, 'tastatura': 200, 'cablu HDMI': 10, 'cooler': 40,
        'boxe mici': 80, 'sistem audio 5.1': 350, 'stick usb': 90, 'mouse pad': 70}

lowest_price = 10000000000
lowest_product = ''
for produs, pret in dict.items():
    if lowest_price > pret and pret >= 100:
        lowest_price = pret
        lowest_product = produs
print(lowest_product)

list = []
i = 0
while i <= 109:
    list.append(i)
    i += 1

count = list.count(0)

print(count)

count = 0
for i in range(0, 110):
    for j in str(i):
        if j == '0':
            count += 1
print(count)

for i in range(0, 110):
    print(i)

correct_answer = "Tesla"
input_answer = input("Please guess the company of the electric car:\n")


def car_guess():
    if correct_answer == input_answer:
        print("Correct")
    else:
        car_guess()





#tax = 0
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
