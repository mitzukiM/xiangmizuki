some_number = []
total = 0

while True:
    some_number = int(input('Введіть число : '))
    total += some_number

    if some_number == 0:
        print("Сума чисел:", total)
        break
