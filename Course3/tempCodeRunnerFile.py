
list_3=["a", "b", "c", "a", "d", "e", "b", "a"] 

final_list = list(dict.fromkeys(list_3))
final_list.remove("a")

print(final_list)
