"""Основы Python (Часть 1)"""
"""1 .Дана строка, состоящая из слов, разделенных пробелами. (Вот 4 варианта тестовых данных для программы: 
‘Hello world’, ‘a b c’, ‘test’, ‘test1 test2 test3 test4 test5’). Определите, сколько в ней слов."""

some_str = 'Hello world, a b c, test, test1 test2 test3 test4 test5'
clean_str = some_str.replace(',', '')
print(len(clean_str.split()))