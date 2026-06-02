import random


def create_matrix(rows, cols):
    return [
        [random.randint(-20, 20) for _ in range(cols)]
        for _ in range(rows)
    ]


def show_matrix(matrix):
    print("\nМатрица:")

    for line in matrix:
        print(line)


def main():
    try:
        rows = int(input("Количество строк: "))
        cols = int(input("Количество столбцов: "))

        if rows < 2 or cols < 1:
            print("Нужно минимум 2 строки и 1 столбец")
            return

        matrix = create_matrix(rows, cols)

        show_matrix(matrix)

        min_value = min([min(row) for row in matrix])

        second_row = matrix[1]

        first_column = []

        for row in matrix:
            first_column.append(row[0])

        print(f"\nМинимальный элемент: {min_value}")
        print(f"Вторая строка: {second_row}")
        print(f"Первый столбец: {first_column}")

    except ValueError:
        print("Ошибка: вводите только целые числа")


if __name__ == "__main__":
    main()
