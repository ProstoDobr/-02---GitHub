year = int(input('Введите год: '))
if year % 400 == 0:
    flag = True
elif year % 100 == 0:
    flag = False
elif year % 4 == 0:
    flag = True
else:
    flag = False
if flag:
    print(f'{year} год високосный')
else:
    print(f'{year} год НЕ високосный')