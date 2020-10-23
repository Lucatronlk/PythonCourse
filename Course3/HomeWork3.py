# 1. De cate ori apare numarul 8 in lista?

list = [1, 10, 9, 8, 8, 7, 8, 11, 2, 7, 89, 8, 90,24, 8, 5] 

my_list = {i:list.count(i) for i in list}
print(my_list)

#Generati primele 50 de numere in ordine descrescatoare

list_2 = []
i = 0
while i < 50:
    i += 1
    list_2.append(i)
    
list_2.sort(reverse=True)
    
print(list_2)

#3 Creati o noua lista care sa fie ca cea de mai sus dar fara litera a 

list_3=["a", "b", "c", "a", "d", "e", "b", "a"] 

final_list = list(dict.fromkeys(list_3))
final_list.remove("a")

print(final_list)
