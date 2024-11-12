"""Основы Python (Часть 1)"""
"""4. Дана строка. Замените в этой строке все появления буквы h на букву H, кроме первого и последнего вхождения.
Подсказка: использовать метод replace с параметрами. 
Например, дано: ‘hhhabchghhh’, должно быть: ‘hHHabcHgHHh’"""

some_str = 'hHHabcHgHHh'

first_h = some_str.find('h')
last_h = some_str.rfind('h')

left_part = some_str[:first_h + 1]
middle_part = some_str[first_h + 1:last_h]
right_part = some_str[last_h:]

middle_part = middle_part.replace('h', 'H')

result = left_part + middle_part + right_part

print(result)
