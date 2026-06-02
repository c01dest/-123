#задача 1 с покупками
price1 = 250  
price2 = 150
print("Общая стоимость:", price1 + price2)

print("ㅤ")

#задача 2 с прямоугольником

side_a = 5
side_b = 10
print("Площадь фигуры равна:", (side_a * side_b))

print("ㅤ")

#задача 3 с средним баллом
scores = [5, 4, 5]
print("Средняя оценка:", round(sum(scores) / len(scores), 2))

print("ㅤ")

#задача 4 с временем
total_sec = 125
min_count = total_sec // 60
sec_left = total_sec % 60
print("Результат:", sec_left, "секунд и", min_count, "минуты")

print("ㅤ")

#задача 5 с конфетами

all_sweets = 20
kids = 3
print("Каждому достанется по", all_sweets // kids, "конфет, остаток составит", all_sweets % kids, "конфет")

print("ㅤ")

#задача 6 с степенями

num_sq = 7 ** 2
num_cb = 3 ** 3
print("Результат возведения в квадрат:", num_sq, ", в куб:", num_cb)

print("ㅤ")

#задача 7 (1) с итоговой ценой со скидкой и налогом
base_price = 1200
disc_rate = 0.15
tax_rate = 0.2
print("Цена со скидкой: ", base_price * (1 - disc_rate))
print("Финальная стоимость: ", base_price - (base_price * (1 - disc_rate)) + (base_price * tax_rate))

print("ㅤ")

#задача 8 (2) с конвертации времени
sec_amount = 3665
hh = sec_amount // 3600
mm = (sec_amount % 3600) // 60
ss = sec_amount % 60
print("Формат времени= ", hh, ":", mm, ":", ss)

print("ㅤ")
print("Дальше вам надо вводить значения")
print("ㅤ")

#задача 9(3) с имт
user_weight = int(input("Укажите ваш вес в кг: "))
user_height = int(input("Укажите ваш рост в см: "))

bmi = round(user_weight / (user_height / 100) ** 2, 1)
print("Индекс массы тела составил:", bmi)
print("ㅤ")

#задача 10(4) с числом
user_val = int(input("Введите любое трехзначное число: "))
digit1 = user_val // 100
digit2 = (user_val // 10) % 10
digit3 = user_val % 10
print("Сумма всех цифр:", digit1 + digit2 + digit3)
print("ㅤ")

#задача 11 (5) с курсом
currency_rate = 90.5
usd_amount = int(input("Укажите сумму долларов для покупки: "))
fee = 0.025
final_pay = usd_amount * currency_rate * (1 + fee)
print("Полная стоимость с учетом комиссии:", round(final_pay, 2))
