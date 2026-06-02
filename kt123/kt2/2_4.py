import random


def create_array(size, min_num=-50, max_num=50):
    return [random.randint(min_num, max_num) for _ in range(size)]


def main():
    try:
        size = int(input("Введите размер массива: "))

        numbers = create_array(size)

        print("\nМассив:")
        print(numbers)

        count_div3 = 0

        even_numbers = []

        for number in numbers:

            if number % 3 == 0:
                count_div3 += 1

            if number % 2 == 0:
                even_numbers.append(number)

        if len(even_numbers) > 0:
            average = sum(even_numbers) / len(even_numbers)
        else:
            average = 0

        print("-" * 30)
        print(f"Чисел, кратных 3: {count_div3}")

        if even_numbers:
            print(f"Среднее четных чисел: {average:.2f}")
        else:
            print("Четных чисел нет")

    except ValueError:
        print("Ошибка: нужно ввести целое число")


if __name__ == "__main__":
    main()
