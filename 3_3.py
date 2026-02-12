sum = 0
chislo = 0

while True:
    try:
        x = float(input())
        
        if x % 2 == 0:
            even_sum += x
            even_count += 1
            
        if x == 100:
            break

    except ValueError:
        continue

print(even_sum / even_count)