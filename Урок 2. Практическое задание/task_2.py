"""
2.	Посчитать четные и нечетные цифры введенного натурального числа.
Например, если введено число 34560, то у него 3 четные цифры
(4, 6 и 0) и 2 нечетные (3 и 5).

Подсказка:
На каждом шаге вам нужно 'доставать' из числа очередную цифру
и смотреть является ли она четной или нечетной. При этом увеличиваем соответствующий счетчик
Пока все числа не извлечены рекурсивные вызовы продолжаем
Условие завершения рекурсии - все числа извлечены

Используем операции % //, НЕ ИСПОЛЬЗУЕМ ОПЕРАЦИИ ВЗЯТИЯ ЭЛЕМЕНТА ПО ИНДЕКСУ

Пример:
Введите число: 123
Количество четных и нечетных цифр в числе равно: (1, 2)

Решите через рекурсию. Решение через цикл не принимается.
Для оценки Отлично в этом блоке необходимо выполнить 5 заданий из 7
"""


def counter(number, even=0, not_even=0):
	if number == 0:
		return even, not_even
	if (number % 10) % 2 == 0:
		return counter(number // 10, even + 1, not_even)
	else:
		return counter(number // 10, even, not_even + 1)

		
try:
	number = int(input("Введите число: "))
except ValueError:
	print("Некорректный ввод!")
else:
	print("Количество четных и нечетных цифр в числе равно:", counter(number))
