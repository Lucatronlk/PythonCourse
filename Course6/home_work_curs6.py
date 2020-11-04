# 1. Find all numbers between 2000 and 3200 which are divisible by 7 but are not a multiple of 5

numbers=[]

for x in range(2000, 3200):
    if(x % 7 == 0) and ( x % 5 == 1):
        numbers.append(x)

print(numbers)


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

def vertical_lines ( size ):
    return "|   " * size + "|\n"

def gameboard ( size ):
    board = """"""
    for i in range(size):
        board += horizontal_line(size)
        board += vertical_lines(size)
    board += horizontal_line(size)
    return board

if __name__ == "__main__":
    size = int(input("What size game board do You want? "))
    print(gameboard(size))



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