def main():
    try:
      
        n = int(input("Введите количество элементов массива: "))

        if n < 2:
            print("Массив слишком мал для поиска пары чисел.")
            return

        array = []
        print(f"Введите {n} чисел(ла) по одному:")

       
        for i in range(n):
            val = int(input(f"Элемент {i+1}: "))
            array.append(val)

     
        print(f"\nВаш массив: {array}")

      
        found_zeros = False
        
       
        for i in range(len(array) - 1):
            if array[i] == 0 and array[i+1] == 0:
                found_zeros = True
                break  

      
        if found_zeros:
            print("Результат: Да, в массиве есть два подряд идущих нуля.")
        else:
            print("Результат: Нет, двух подряд идущих нулей не найдено.")

    except Exception as e:
        print(e)

main()