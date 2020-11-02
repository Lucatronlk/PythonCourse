# 3: Intr-un fisier definiti o functie care verifica daca un numar e par sau impar. 
# In alt fisier, verificati un numar dat de user daca e sau nu par folosind functia definita in celalalt fisier.

def is_odd(number):
    if int(number) % 2 == 0:
        return False
    else:
        return True    