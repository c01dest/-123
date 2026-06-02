# читаем а, b, k из одной строки
start_num = int(input("введите число a: "))
end_num = int(input("введите число b: "))
target_k = int(input("введите число k: "))

matches = []
# b + 1 чтобы включить правую границу
for number in range(start_num, end_num + 1):
    total_mult = 1
    for char in str(number):
        if char != '0':
            total_mult *= int(char)
    
    if total_mult == target_k:
        matches.append(number)

if not matches:
    print("подходящих чисел нет")
else:
    # количество, минимум и максимум
    print("длина списка:", len(matches), ", минимум:", min(matches), ", максимум:", max(matches))
