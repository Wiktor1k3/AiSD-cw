a = []
b = 0

while b != "":
    b = input("Podaj wartość:")
    if b != "":
        a.append(b)
a = tuple(a)
print(a)
