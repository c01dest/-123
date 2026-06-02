def has_double_zero(numbers):
    for index in range(len(numbers) - 1):

        if numbers[index] == 0 and numbers[index + 1] == 0:
            return True

    return False


def main():
    try:
        size = int(input("Введите размер массива: "))

        if size < 2:
            print("Нужно минимум 2 элемента")
            return

        numbers = []

        print(f"Введите {size} элементов:")

        for i in range(size):
            value = int(input(f"Число {i + 1}: "))
            numbers.append(value)

        print("\nМассив:", numbers)

        result = has_double_zero(numbers)

        if result:
            print("Есть два нуля подряд")
        else:
            print("Два нуля подряд не найдены")

    except ValueError:
        print("Ошибка: нужно вводить числа")


if __name__ == "__main__":
    main()
