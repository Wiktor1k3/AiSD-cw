suma = 0
while suma != 100:
    a = int(input("Podaj liczbę:"))
    suma +=a
    if (suma > 100):
        print("suma:" + str(suma))
        break
if(suma==100):
    print("suma = 100")