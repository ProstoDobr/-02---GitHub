print('''Доступные единицы:
1 - Километры
2 - Метры
3 - Сантиметры
4 - Милиметры
5 - Мили
6 - Ярды''')
source = int(input('Исходные единицы (1-6): '))
target = int(input('Нужные единицы (1-6): '))
value = float(input('Введите значение: '))
to_meters = {1: 1000,
             2: 1,
             3: 0.01,
             4: 0.001,
             5: 1609.344,
             6: 0.9144}
meters = value * to_meters[source]
result = meters / to_meters[target]
units = ['км', 'м', 'см', 'мм', 'мили', 'ярды']
print(f'{value} {units[source - 1]} = {result:.6f} {units[target - 1]}')