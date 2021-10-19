'''
Задача 1
Вывести на экран циклом пять строк из нулей, причем каждая строка должна быть пронумерована.
'''
# Не указано сколько нулей
null_num=input('Введите количество нулей в строке: ')
for n,i in enumerate(range(5)):
    print(n,(str(0)*5))

'''
Задача 2
Пользователь в цикле вводит 10 цифр. Найти количество введеных пользователем цифр 5.
'''
counter=0
for i in range(10):
    number=input('Введи число: ')
    if int(number)==5:
        counter+=1
    else:
        continue
print(counter)

'''
Задача 3
Найти сумму ряда чисел от 1 до 100. Полученный результат вывести на экран.
'''
sum = 0

for i in range(1,101):
    sum+=i
print(sum)

'''
Задача 4
Найти произведение ряда чисел от 1 до 10. Полученный результат вывести на экран.
'''

prod = 1

for i in range(1,101):
    prod*=i
print(prod)

'''
Задача 5
Вывести цифры числа на каждой строчке.
'''

# Вариант в уроке
integer_number = 2129

print(integer_number%10,integer_number//10)

while integer_number>0:
    print(integer_number%10)
    integer_number = integer_number//10

# Альтернативный костыль-вариант:
str_number=str(integer_number)
for i in str_number:
    print(int(i))



'''
Задача 6
Найти сумму цифр числа.
'''

chislo=1234
summa=0
for i in str(chislo):
    summa+=int(i)
print(summa)

# или
chislo=1234
summa=0
while chislo!=0:
    new_chislo=chislo//10
    slagaemoe=chislo%10
    summa+=slagaemoe
    chislo=new_chislo
    if chislo==0:
        break
print(summa)



'''
Задача 7
Найти произведение цифр числа.
'''
chislo=1234
prod=1
while chislo!=0:
    new_chislo=chislo//10
    mnozitel=chislo%10
    prod*=mnozitel
    chislo=new_chislo
print(prod)

'''
Задача 8
Дать ответ на вопрос: есть ли среди цифр числа 5?
'''
integer_number = 213413
while integer_number>0:
    if integer_number%10 == 5:
        print('Yes')
        break
    integer_number = integer_number//10
else: print('No')

# или
for i in str(integer_number):
    if i==5:
        print('Yes')
        break
    else:
        print('Nope')

'''
Задача 9
Найти максимальную цифру в числе
'''
import numpy as np
listik=[]
some_num=12345
for i in str(some_num):
    listik.append(int(i))
print(np.max(listik))

'''
Задача 10
Найти количество цифр 5 в числе
'''
counter=0
some_num=123456
for i in str(some_num):
    if i == str(5):
        counter+=1
print(counter)


