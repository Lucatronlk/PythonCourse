# 1. Find all numbers between 2000 and 3200 which are divisible by 7 but are not a multiple of 5

numbers=[]

for x in range(2000, 3200):
    if(x % 7 == 0) and ( x % 5 == 1):
        numbers.append(x)

print(numbers)

#Roberto`s Solution
i = 2000 
list=[]
while i < 3200:
    if i % 7 == 0 and i % 5 != 0:
        list.append(i)
        i += 1   
print(list)

# 2. Draw a game board with the size given by the user. If the user says 3 and 4, it should look like this 
#  --- --- --- --- 
# |   |   |   |   |
#  --- --- --- ---
# |   |   |   |   |
#  --- --- --- --- 
# |   |   |   |   |
#  --- --- --- ---

def horizontal_line ( size ):
    return " ---" * size + " \n"

def vertical_lines ( size_v ):
    return "|   " * size + "|\n"

def gameboard ( size, size_v ):
    board = """"""
    for i in range(size, size_v):
        board += horizontal_line(size)
        board += vertical_lines(size_v)
    board += horizontal_line(size)
    board += vertical_lines(size_v)
    return board

if __name__ == "__main__":
    size = int(input("What horizontal size game board do You want? "))
    size_v = int(input("What vertical size game board do You want? "))
    print(gameboard(size, size_v))

#Roberto`s Solution

x = input('Give the row number ')
y = input('Give the column number ')

top = ' ---'
side = '|   '

i = 0 
j = 0

while i < int(x):
  print(top * int(y))
  print(side * int(y) + '|')
  i += 1


# 3. Generate the first 30 numbers of the Fibonacci sequence. The Fibonacci sequence is a series of numbers where a number is the addition of the last two numbers. First 2 numbers are 0 and 1, after that list[x] = list[x-1] + list[x-2]
# The result should be this: 0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233, 377, 610, 987, 1597, 2584, 4181

def printFibonacciNumbers(n): 
      
    f1 = 0
    f2 = 1
    if (n < 1): 
        return
    for x in range(0, n): 
        print(f2, end = " ") 
        next = f1 + f2 
        f1 = f2 
        f2 = next
          
printFibonacciNumbers(30) 

#Roberto`s Solution

n0 = 0
n1 = 1

x = input("How many Numbers? ")

list = [n0, n1]
while len(list) < int (x):
    last = n0 + n1
    list.append(last)
    n0 = n1
    n1 = last

print(list)   

# Second Option

x = input("How many Numbers? ")
list = [0 , 1]
while len(list) < int(x):
    new = list[len(list) - 1 ] + list[len(list) - 2 ]
    list.append(new)

print(list)    
