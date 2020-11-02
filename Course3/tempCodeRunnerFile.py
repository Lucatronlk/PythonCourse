user_number = input("Give me a number between 1 and 10 ")
print(user_number)

list_number = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10']
is_user_input_right = False
for element in list_number:
    if user_number == element:
        is_user_input_right = True
        break

if is_user_input_right:
    print('Your number is correct')
else:
    print('Your number is not good')