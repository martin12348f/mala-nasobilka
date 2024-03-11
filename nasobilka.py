import random

def nasobeni(a, b):
    return a * b

def deleni(a, b):
    return a / b

def scitani(a, b):
    return a + b

def odcitani(a, b):
    return a - b

def vyhodnoceni(vysledek, porovnani):
    if vysledek == porovnani:
        print("Jste ale šikula!")
        return True
    else:
        print("Ach, škoda, zkuste to znovu.")
        return False

spravne = 0

for _ in range(9):  
    x = random.randint(1, 10)
    y = random.randint(1, 10)
    
    vysledek = nasobeni(x, y)
    print(x, "*", y, "=")
    porovnani = int(input())

    if vyhodnoceni(vysledek, porovnani):
        spravne += 1  
    print("Celkový počet správných odpovědí:", spravne)


    vysledek = deleni(x, y)
    print(x, "/", y, "=")
    porovnani = int(input())

    if vyhodnoceni(vysledek, porovnani):
        spravne += 1  
    print("Celkový počet správných odpovědí:", spravne)



    vysledek = scitani(x, y)
    print(x, "+", y, "=")
    porovnani = int(input())

    if vyhodnoceni(vysledek, porovnani):
        spravne += 1  
    print("Celkový počet správných odpovědí:", spravne)



    vysledek = odcitani(x, y)
    print(x, "-", y, "=")
    porovnani = int(input())

    if vyhodnoceni(vysledek, porovnani):
        spravne += 1  
    print("Celkový počet správných odpovědí:", spravne)






