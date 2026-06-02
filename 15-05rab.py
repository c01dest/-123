# def plus (a,b):
#      return a + b
# def minus (a,b):
#      return a - b
# def multiply (a,b):
#      return a * b
# def divide (a,b):
#      if not b or not a:
#          return "на ноль делить нельзя"
#      return a / b
# def square(a):
#      return a * a


# result1 = plus(5, 3)
# result2 = minus(5, 3)
# result3 = multiply(5, 3)
# result4 = divide(5, 3)
# result5 = square(5)

# задание 1
def format_price(cost, currency="руб", disc=0):
    if cost < 0 or disc < 0 or disc > 100:
        return "Ошибка: неверные данные"
    final_sum = cost - (cost * (disc / 100))
    return f"{final_sum:.2f} {currency}".strip()

print(format_price(1500))
print(format_price(1500, "", 20))
print(format_price(-100))
print(format_price(1000, "₽", 150))

# задание 2
nums =
