import math

print('Введите коофиценты квадратного уравнения при виде "D = b2-4ac" ')

a = float(input("Введите коофицент A"))
b = float(input("Введите коофицент B"))
c = float(input("Введите коофицент C"))
D = b * 2 - 4 * a * c

if D > 0:
    X1 = (-b + math.sqrt(D)) / (2*a)
    X2 = (-b - math.sqrt(D)) / (2*a)
    print(f"Уравнение имеет два корня:\nx1 = {X1}\nx2 = {X2}")

elif D == 0:
    X = -b / (2*a)
    print(f"Уравнение имеет один корень:\nx = {X}")

else:
    print("Уравнение не имеет действительных корней (D < 0).")
