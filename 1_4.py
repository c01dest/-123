import random

def main():
    try:
    
        n = int(input("Введите количество элементов массива: "))
        
    
        min_val = -50
        max_val = 50

        array = [random.randint(min_val, max_val) for _ in range(n)]
        
        print(f"\nСгенерированный массив:\n{array}")

   
        count_div_3 = 0 
        even_sum = 0    
        even_count = 0   

     
        for num in array:
        
            if num % 3 == 0:
                count_div_3 += 1
         
            if num % 2 == 0:
                even_sum += num
                even_count += 1

      
        if even_count > 0:
            even_avg = even_sum / even_count
        else:
            even_avg = 0

     
        print("-" * 30)
        print(f"Количество чисел, делящихся на 3: {count_div_3}")
        
        if even_count > 0:
            print(f"Среднее арифметическое четных чисел: {even_avg:.2f}")
        else:
            print("В массиве не найдено четных чисел.")

    except Exception as e:
        print(e)

main()