# #задание 1
# val = int(input("введите любое число: "))
# if val % 2 != 0:
#      print("число нечетное")
# else:
#      print("число четное")

# print("ㅤ")

# #задача 2 с ростом
# height = int(input("введите ваш рост в см: "))
# if height > 119:
#      print("проход разрешен!")
# else:
#      print("рост слишком мал!")

# print("ㅤ")

# #задача 3 с числами
# value_3 = int(input("введите число: "))
# if value_3 < 0:
#      print("число отрицательное")
# else:    
#      print("число положительное")
# print("ㅤ")

# #задача 4 с паролем
# psw = input("введите код доступа: ")
# if psw == "password123":
#      print("доступ одобрен")
# else:    
#      print("неверный код доступа")

# print("ㅤ")

# #задача 5 с ценами

# total_cost = int(input("введите сумму покупки: "))
# if total_cost >= 1000:
#      print("вам доступна скидка 10%!")
#      total_cost = total_cost * 0.9
#      print("сумма к оплате: ", total_cost)
# else:   
#      print("скидка не применяется, сумма к оплате: ", total_cost)

    #задание 6
# check_year = int(input("укажите год: "))
# if check_year % 400 == 0:
#      print("год високосный")
# elif check_year % 100 == 0:
#      print("год не високосный")
# elif check_year % 4 == 0:
#      print("год високосный")
# else:
#      print("год не високосный")

# print("ㅤ")

# #задание 7
# s1 = int(input("сторона 1: "))
# s2 = int(input("сторона 2: "))
# s3 = int(input("сторона 3: "))
# if s1 == 0 or s2 == 0 or s3 == 0:
#      print("такого треугольника нет")
# elif s1 == s2 == s3:
#      print("треугольник равносторонний")
# elif s1 != s2 and s1 != s3 and s2 != s3:
#      print("треугольник разносторонний")
# else:
#      print("треугольник равнобедренный")


coord_x = int(input("введите координату x: "))
coord_y = int(input("введите координату y: "))

# Изменили порядок проверки четвертей (сначала 1, потом 4, 2, 3) и поменяли ветку else
if coord_x > 0 and coord_y > 0:
    print("точка находится в первой четверти")
elif coord_x > 0 and coord_y < 0:
    print("точка находится в четвертой четверти")
elif coord_x < 0 and coord_y > 0:
    print("точка находится во второй четверти")
elif coord_x < 0 and coord_y < 0:
    print("точка находится в третьей четверти")
elif coord_x == 0 and coord
