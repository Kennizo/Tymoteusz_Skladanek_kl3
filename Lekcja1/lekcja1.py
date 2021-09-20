import random

dolny_zakres = int(input("Najmniejsza możliwa liczba:\n"))
górny_zakres = int(input("Najwieksza możliwa liczba:\n"))

n = random.randint(dolny_zakres, górny_zakres)

tries = int(input("Ile prób chcesz mieć?:\n"))

while tries > 0:
    input_number = int(input("Podaj liczbę od " + str(dolny_zakres) + " do " + str(górny_zakres)))
    if dolny_zakres < input_number < górny_zakres:
        if input_number > n:
            print("Liczba podana przez ciebie jest za duża.\n")
            tries -= 1
        elif input_number < n:
            print("Liczba podana przez ciebie jest za mała.\n")
            tries -= 1
        else:
            print("Wygrałeś.\n")
            break

