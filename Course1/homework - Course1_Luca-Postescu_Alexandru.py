#  Bool/comparison operators:
#  1. write 3 comparisons which are True
#  2. write 3 comparisons which are False
#  3. write a comparison in a function and call it 3 times with different parameters
#  4. check the functions output using if

comp_1 = 10
comp_2 = 20
comp_3 = 30
comp_4 = 40
comp_5 = 50

print(comp_1 < comp_2)
print(comp_2 > comp_1)
print(comp_3 > comp_2)

print(comp_3 < comp_1)
print(comp_2 < comp_1)
print(comp_4 > comp_5)

comp = comp_1


# comp = comp_2
# comp = comp_3

def comp_func(comp):
    if comp > 60:
        print('Ceva')
    elif comp < 60:
        print('AsaCeva')
    else:
        print('Altceva')


#  Operations with int/float:
#  1. Write a function which makes the sum of 3 ints
#  2. Write a function which computes 2 power to the specified variable 
#  3. Write a function which makes the sum of 4 floats
#  4. Write a function which makes diff of 2 floats & multiplies it with a int 
#  5. Write a function which computes how many apples go into a specified number of boxes
#  6. Check the functions output using if 

# 1
def sum_int(a, b, c):
    sum = a + b + c

    if a != b != c:
        sum = a + b + c
        return sum
    if a == b == c:
        sum = sum * 3
        return sum


print(sum_int(1, 2, 3))
print(sum_int(3, 3, 3))


# 2
def pow_int(a, b):
    pow = a ** b
    return pow


print(pow_int(3, 3))


# 3

def sum_float(a, b, c, d):
    sum = a + b + c + d
    return sum


print(sum_float(12.1, 13.4, 2.3, 4.8))

# 4 Write a function which makes diff of 2 floats & multiplies it with a int

f = 8.9
l = 21.8
i = 12

diff = f - l
print(diff)

multi = diff * i

print(multi)


# 5 Write a function which computes how many apples go into a specified number of boxes

def number_apples(cos, mar_rosu, mar_verde):
    return (mar_rosu + mar_verde) - cos + 1


if __name__ == '__main__':
    cos = 3
    mar_rosu = 6
    mar_verde = 3

print("Nr Total de Mere tinut este =",
      number_apples(cos, mar_rosu, mar_verde))

#  Operations with strings:
#  0. Select the 5th letter of 3 Strings 
#  1. Make 3 substrings with only the first 6 chars of a String
#  2. Make 3 substrings with only the last 3 chars of a String
#  3. Make 3 substrings without the first 4 chars of a String
#  4. Put together 4 strings 
#  5. Show the same string 15 times 
#  6. Define functions for all the exercises above
#  7. Check the output of the functions with if

# 0
print("uncuvant"[5])
print("altcuvant"[5])
print("cuvantulcuvantului"[5])

# 1
string_1 = "exercises"
string_2 = "functions"
string_3 = "substrings"
string_4 = "letter"

print(string_1[0:5])
print(string_2[0:5])
print(string_3[0:5])

# 2

print(string_1[-3:])
print(string_2[-3:])
print(string_3[-3:])

# 3

print(string_1[4:])
print(string_2[4:])
print(string_3[4:])

# 4

print(string_1 + string_2 + string_3 + string_4)

# 5

print(string_1 * 15)


#  Functions and ifs:
#  1. Calculate tax for a apartments based on space
#     a. 20mp => 100ron
#     b. 50mp => 300ron
#     c. 100mp => 500ron
#     d. 200mp => 2000ron
#  2. Calculate tax on a machine based on its engine
#  3. Check the functions output using if 

# 1

def tax_appart(tax):
    if space == 20:
        return "Taxa este de 100 ron"
    elif space == 50:
        return "Taxa este de 300 ron"
    elif space == 100:
        return "Taxa este de 500 ron"
    elif space == 200:
        return "Taxa este de 2000 ron"


space = 20
print(tax_appart(space))


# 2

def tax_car(tax):
    if engine < 1.9:
        return " Taxa motor este de 50 lei"
    elif engine >= 2.0:
        return "Taxa motor este de 90 lei"
    elif engine >= 3.0:
        return "Taxa motor este de 150 lei"
    elif engine >= 4.0:
        return "Taxa de motor este 300 lei"
    elif engine > 5.0:
        return "Taxa de motor este 500 lei"


engine = 2.5

print(tax_car(engine))
