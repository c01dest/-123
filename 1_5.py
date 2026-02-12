text = input("Введите текст: ").strip()


words = text.split()


all_correct = True
for word in words:
    if word and not word[0].upper() in ['A', 'B', 'C']:
        all_correct = False
        break

if all_correct and words:
    print("YES")
else:
    print("NO")