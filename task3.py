#Напишите программу для. проверки истинности утверждения
# ¬(X ⋁ Y ⋁ Z) = ¬X ⋀ ¬Y ⋀ ¬Z для всех значений предикат.

sum = 0
for x in range(0, 2):
    for y in range(0, 2):
        for z in range(0, 2):
            if not(x or y or z) == ((not x) and (not y) and (not z)):
                print(True)
            else:
                print(False)
            sum += 1 
print('Количество предикат', sum)