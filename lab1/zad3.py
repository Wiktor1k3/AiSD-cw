def funk(a, b, c):
    return (a*100 + b - c)
a = input("Pierwsze dwie cyfry roku:")
b = input("Ostatnie dwie cyfry roku:")
c = input("Wiek:")

print("Rok urodzenia:"+ str(funk(int(a),int(b),int(c))))