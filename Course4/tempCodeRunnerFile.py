print("Va rog introduceti un nr intre 50 si 100")
user_numb = input()

if user_numb < 50:
    print("Your number is bellow 50")
elif user_numb > 100:
    print ("Your number is above 100")    
elif user_numb.isalpha():
    print("You should enter a number")
