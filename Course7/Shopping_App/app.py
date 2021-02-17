#   Create a mini application which mimics a shooping website (Amazon, emag)
#   This document provides guidelines to implementing this application. This is not the only way to do it, it is not even the best way to do it :))
#   Commands will be given using the terminal, we can read the params with 
#   import sys
#   sys.argv # a list with all the params from the terminal

#Procedural 
from os import close
import sys
import os 

arguments = sys.argv[1:]

def  get_username_file(username):
    return 'user_' + username

def does_file_exists(file_path):
    try:
        file = open(file_path)
        file.close
        return True
    except FileNotFoundError:
        return False       

if arguments[0] == 'user' and arguments[1] == 'add':
    try:
        file = open(get_username_file(arguments[2]))
        file.close()
        print('The username already exists')
    except:    
        file = open(get_username_file(arguments[2]), 'w' )
        file.close()
        print('User sucesfully created')


if arguments[0] == 'user' and arguments[1] == 'remove':
    try:
        os.remove(get_username_file(arguments[2]))
    except FileNotFoundError:
        print('The user does not exist')


if arguments[0] == 'user' and arguments[1] == 'edit':
    old_username = arguments[2]
    new_username = arguments[3]

    if does_file_exists(get_username_file(old_username)):
        if not does_file_exists(get_username_file(new_username)):
            file = open(get_username_file(new_username), 'w')
            file.close()
            os.remove(get_username_file(old_username))
        else:
            print('New Username already exists') 
    else:
        print('User does not exists')           

    







#   Commands we can give the program:
# we can add a user with a specified username: python3 app.py user add <username>, error if the username already exists
#   - we create a file <username>, if we already have a file we print a message describing the problem 
#   - to check if a file exists, we try to read it; it will raise an exception if the file does not exist
# we can delete a user specifying its username: python3 app.py user remove <username>, error if the username does not exist
#   - we remove the file <username>, if it does not exist we print a message describing the problem
#   - we did not learn how to remove it, but i will show an example (it's really simple)
#        import os
#        os.remove("file.txt") # if the file does not exist, it will raise an exception 
# we can edit a user's username: python3 app.py user edit <old_username> <new_username>, error if the old_username does not exist, error if the new_username already exists
#   - if the <old_username> file does not exist, it means the user does not exist so we print an error
#   - if the file <new_username> exists, it means the <new_username> is not available so we print an error
#   - read content from <old_username> and write it to file <new_username>  
#   - remove file <old_username>
# we can add a product and specify how much of it we have in stock: python3 app.py product add <product_name> <price> <stock_number>, error if product_name already exists, error if price is not int or float, error if stock_number is not int
#   - we will store the products in a file named products.txt (very original, I know); check if the file exists, if not create it 
#   - append a new line with the format "<product_name>;<price>;<stock_number>\n"
#   - before doing an append, we should go through all the lines and check if there is already a product
#   - to get all the lines, read the file and store it in a variable; after that: `all_lines = file_content.split('\n')`, this will give us a list, each element will be a line from the file 
#   - to get the product_name from a line, `product_name = line.split(';')[0]`
       
# we can delete a product: python3 app.py product delete <product_name>, error if the product name does not exist
#   - we need to open the file `products.txt`, if the file does not exist print an error
#   - we need to go through all the lines from the file and see if we can find the product name, if we do not find it print an error
#   - if we find the product_name, we need to remove it from the list `all_lines` and rewrite the file without the product name; to rewrite the file we can delete it, and go through all the lines again and append each one to the file with '\n' at the end of the line
       
# we can add more items of a product, it will increase the stock number: python3 app.py product add stock <product_name> <new_number_of_items>, error if product_name does not exist, error if new_number is not int
#   - we check if the product_name exists by going through all the lines again, if not we print an error
#   - we identify the line with our product_name, we replace the stock number with the new one new_stock = old_stock + new_number_of_items 
#   - we replace this line in all_lines 
#   - we rewrite the whole products file again
# we can remove items from stock, it will decrease the stock number: python3 app.py product remove stock <product_name> <number_of_items_to_be_removed>, error if product_name does not exist, error if number is not int, error if we have less numbers in stock than the number of items to be removed
#   - same as add, but we decrease the number of stocks
#   - if the new stock_number is less than 0, we do not modify the file products.txt and print an error 
# we can change the price a product: python3 app.py product edit <product_name> <new_price>, error if product does not exist, error if new_price is not int or float
#   - same as add/decrease of stock number, but we modify the price field
#   - we need to check the price is float
# a user can add a product to wishlist: python3 app.py user wishlist add <username> <product_name>, error if the username does not exist, error if the product name does not exist
#   - we check if the <username> file exists, we check if <product_name> exists in products.txt 
#   - every user has a file with its username, we append <product_name> to a new line
# a user can delete a a product from wishlist: python3 app.py user wishlist remove <username> <product_name>, error if the username does not exist, error if the product_name does not exist
#   - check if <username> file exists
#   - go through all the lines from the file <username> and see if <product_name> exists, if not print error
#   - if we find the line, remove the element from all_lines and rewrite the file <username>
# a user can order an item: python3 app.py user order <username> <product_name> <number_of_items>, delete <product_name> from wishlist, remove item_numbers from products, error if there are not enough in stock, error if the username does not exist, error if the product_name does not exist
#   - check if the file <username> exists, if not it means the user does not exist so we print an error
#   - check product_name exists in products.txt
#   - check product has enough items in stock, print an error if not
#   - decrease the number of items in products.txt
#   - delete product_name from wishlist, if it is not in wishlist do not print error