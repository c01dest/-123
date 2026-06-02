import random

def main():
    try:

        rows = int(input("Введите количество строк: "))
        cols = int(input("Введите количество столбцов: "))

        if rows < 2 or cols < 1:
            print("Для корректной работы нужно минимум 2 строки и 1 столбец.")
            return

 
        matrix = [[random.randint(-20, 20) for _ in range(cols)] for _ in range(rows)]

        print("\nСгенерированная матрица:")
        for row in matrix:
            print(row)

  
        minem = min(min(row) for row in matrix)

        
        second = matrix[1]

      
        first = [row[0] for row in matrix]

        print(f"\nМинимальный элемент: {minem}")
        print(f"Вторая строка: {second}")
        print(f"Первый столбец: {first}")

    except Exception as e:
        print(e)

main()
