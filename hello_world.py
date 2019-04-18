print("Sprawdz, czy podana liczba jest liczba pierwsza!")

x = input("Podaj liczbe: ")



def liczby(x, z=1):
    while int(x) > z:
        if int(x) / z != 0:
            z += 1
            if int(x) == z:
                return "To jest liczba pierwsza!"
        else:
            return "To nie jest liczba pierwsza!"


print(liczby(x, z=1))

