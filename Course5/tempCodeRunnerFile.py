dict1 = {'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 'A'}
#    a. remove last element

dict1.popitem()
print(dict1)

#    b. print all keys for the values above 2

for key, value in dict1.items():
    if value > 2:
        print(key)