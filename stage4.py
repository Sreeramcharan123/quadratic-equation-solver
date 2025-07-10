import math

with open("input2.txt", "r") as file:
    lines = file.readlines()
for line in lines:
    a, b, c = map(float, line.strip().split())
    print(f"\nEquation: {a}x² + {b}x + {c} = 0")
    d = b**2 - 4*a*c

    if d > 0:
        root1 = (-b + math.sqrt(d)) / (2*a)
        root2 = (-b - math.sqrt(d)) / (2*a)
        print("Two distinct real roots:")
        print("Root 1 =", root1)
        print("Root 2 =", root2)
    elif d == 0:
        root = -b / (2*a)
        print("Two equal real roots:")
        print("Root =", root)
    else:
        real = -b / (2*a)
        imag = math.sqrt(-d) / (2*a)
        print("Complex roots:")
        print(f"Root 1 = {real} + {imag}i")
        print(f"Root 2 = {real} - {imag}i")
