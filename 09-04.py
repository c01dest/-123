steps = 0
while steps < 7:
    print("купи слона")
    steps += 1

x = int(input("введите число a: "))
y = int(input("введите число b: "))
while y > x > 0:
    print("вот список натуральных чисел от a до b: ")
    for num in range(x, y + 1):
        print(num)
    break


# print("купи слона")
# while True:
#      msg = input()
#      print("вот все говорят <" + msg + ">, а ты купи слона")
    
    
print("угадай число от 1 до 7")
while True:

        user_num = int(input())
        
        if user_num > 5:
            print("число меньше")
        elif user_num < 5:
            print("число больше")
        else:   
            print("ты угадал число!")
            print("теперь у тебя 3 попытки, угадай число от 7 до 15")

            limit = 3
            while limit > 0:
                user_num_2 = int(input())
                if user_num_2 > 10:
                    print("число меньше")
                    limit -= 1
                elif user_num_2 < 10:
                    print("число больше")
                    limit -= 1
                else:   
                    print("ты угадал число!")
                    break
                if limit == 0:
                    print("попытки закончились, ты проиграл!")
            break
