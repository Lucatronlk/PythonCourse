print ('Create a new password')
print ()
password = str(input())

def password(user_password):

    if len(password) < 10:
        print ("The password is wery week, you can consider changing it ")
    elif len(password) < 20:
        print ("The Password is moderate.....")
    elif len(password) > 20:
        print("Your password is strong, Good job")