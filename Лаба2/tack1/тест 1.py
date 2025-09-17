from math import sqrt

a, b, c = float(input("Первая сторона: ")), float(input("Вторая сторона: ")), float(input("Третья сторона: ")),
if a + b > c and a + c > b and c + b > a:
    p = (a + b + c) / 2
    S = sqrt(p * (p - a) * (p - b) * (p - c))
    print(f"Площадь треугольника = {S:.2f}")
else:
    print("Такого треугольника не сущестует")