#1: Scrieti un program in python care aduna toate numerele pe care le da user-ul prin terminal

import sys

args = sys.argv
#print(args) 
def is_number(value):
    try:
        int(number)
        return True
    except:
        return False 

numbers = args[1:]
print(numbers)

sum = 0 
for number in numbers:
  if is_number(number):
    sum += int(number)
           
print(sum)    