#1. Задайте переменные разных типов данных:
immutable_var = (3, 'белый', 4.79)
print(immutable_var, type(immutable_var))
#2. Изменение значений переменных:
#immutable_var = ('яблоко', 'банан', 'вишня')
#immutable_var[1] = 'апельсин'
# Попытка изменения элемента  кортежа 'банан' на 'апельсин' привоит к ошибке.
# #поскольку кортежи предназначены для хранения фиксированных наборов значений.
#3. Создание изменяемых структур данных:
mutamutable_list = ('яблоко','банан','вишня')
print(mutamutable_list)
b= list(mutamutable_list)
b[1] = 'тЮпл'
print(b)
# или
bebebe = ([1,2],3)
print(bebebe)
bebebe[0][0] = 2
print(bebebe)