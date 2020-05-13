#!/usr/bin/env python
# coding: utf-8

# Импортируем модуль random для генерации случайных чисел 
import random

# Зададим переменные для работы с границами выборки
list = []    
low = -1
high = 100
iteration = 0

# Сгенерируем случайное натуральное число в диапазоне от 1 до 100
random_digit = random.randint(1, 100) 

# Заполним список натуральными числами от 1 до 100 
for i in range(1, 101):
    list.append(i)
    
    
# Запустим цикл, пока выборка не сократиться до одного числа
while low <= high:
    mid = (low+high) // 2     # Находим середину
    guess = list[mid-1]       # Присвоим переменной guess значение из списка list
    iteration += 1            # Увеличим счётчик попыток на единицу
    
    # Если значение найдено 
    if guess == random_digit:
        print('Загаданное число:', mid)
        print('Количество попыток:', iteration)
        break
        
    # Если "перелёт", уменьшим верхнюю границу выборки 
    if guess > random_digit:
        high = mid-1
    
    # Если "недолёт", увеличим нижнюю границу выборки
    else:
        low = mid+1