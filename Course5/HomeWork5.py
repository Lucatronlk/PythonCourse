#1   Are the following if statements True or False:
#    a. if True and False: --> FALSE
#    b. if False or True: --> TRUE
#    c. if 10 >= 10 and 67 > 66: --> TRUE
#    d. if 10 < 10 and 10 >= 9: --> FALSE
#    e. if -1 < -2 or -2 > -1: --> TRUE
#    f. if True or False and True: --> TRUE
#    g. if True and False or False and True: --> TRUE
#    h. if not True and not False: --> FALSE
#    i. if not True or True: --> TRUE
#    j. if False and not False: --> FALSE



#2. What values should x,y have so the following if statements are True? What about False?
#    a. if x > 6 and x < 12:  -->  TRUE: 7 > 6 and 7 < 12   | FALSE: 6 > 6 and 11 < 12
#    b. if x > 10 or y > 10:  -->  TRUE: 11 > 10 or 9 > 10  | FALSE: 9 > 10 or 8 > 10
#    c. if x < 9 or True:     -->  TRUE: 9 < 9 or True      | FALSE: Cannot be false because one value is true 
#    d. if y > 99 and False:  -->  TRUE: Cannot be true     | FALSE: 99 > 99 and False 
#    e. if x > 10 and x < 10: -->  TRUE: 11 > 10 and 9 < 10 | FALSE:  9 > 10 and 9 < 10
#    f. if not x:             -->  TRUE not False           | FALSE: not True
#    g. if x > 10 or x < 10:  -->  TRUE 11 > 10 or 10 < 10  | FALSE 10 > 10 or 10 < 10
#    h. if x > 12 and x < 18 or y > 4 and not y < 89:  -->    TRUE:  13 > 12 and 13 < 18 or 90 > 4 and not 90 < 89 | FALSE: 11 > 12 and 11 < 18 or 3 > 4 and 3 < 89


#3 Exercises with lists
list1 = [1, 3, 45, -7, 89, 1, 12, 33, 1]
list2 = ["a", "cd", "b", "b", "f", "oj", "Zz"]
list3 = [1, 2, "a", 34, "bgh", "#"]
    
#    a. eliminate all elements from list3

list3.clear()
print(list3)

#    b. eliminate all 3 from list1

list1.remove(3)
list1.remove(33)
print(list1)

# #    c. sort list1 from the biggest number to the lowest

list1.sort(reverse=True)
print(list1)

# #    d. sort list2 without "Zz"
list2.pop()
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


dict1 = {key : val for key, val in dict1.items() if not (isinstance(val, int) and (val > 2))}
print(dict1)

#    d. print all the values remaining

print(dict1)
#    e. remove all remaining elements from dict


dict1.clear()

print(dict1)
