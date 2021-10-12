def funk1(a,b,funk2):
    return funk2(a,b)

def funk2(a, b):
    return (a[0].capitalize() + ". " + b[0].upper()+b[1:])

a = input("Podaj imie:")
b = input("Podaj nazwisko:")

print(funk1(a,b,funk2))