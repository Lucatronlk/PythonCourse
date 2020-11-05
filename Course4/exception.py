try:
    a = int('aaaaaah')
except Exception as error:
    # print(error)
    raise Exception('mesaj de eroare')

print('hello')

try:
    a = int(input("Da un numar"))
except Exception as error:
    raise Exception(' da un numar')

try:
    b = int(input("da un nr 2"))
except Exception as error:
    raise Exception('al doile nr nu e correct')
