import numpy as np

chislo = input('Загадай число от 0 до 99: ')
char_num = input('При делении // на 10 получается число отличное от 0?(да/нет): ')
if char_num == 'да':
    odd_or_not = input('Число, полученное при делении // на 10 делится на 2 без остатка?(да/нет): ')
    if odd_or_not == 'да':
        char_num = input('Первая цифра числа больше 5?(да/нет): ')
        if char_num == 'да':
            cratnost_3 = input('Первая цифра числа кратна 3?(да/нет): ')
            if cratnost_3 == 'да':
                num1 = 6
            else:
                num1 = 8
        else:
            cratnost_4 = input('Первая цифра числа кратна 4?(да/нет): ')
            if cratnost_4 == 'да':
                num1 = 4
            else:
                num1 = 2
    else:
        char_num = input('Первая цифра числа больше 5?(да/нет): ')
        if char_num == 'да':
            cratnost_3 = input('Первая цифра числа кратна 3?(да/нет): ')
            if cratnost_3 == 'да':
                num1 = 9
            else:
                num1 = 7
        else:
            cratnost_3_ = input('Первая цифра числа кратна 4?(да/нет): ')
            if cratnost_3_ == 'да':
                num1 = 3
            else:
                num1 = 1

else:
    num1 = 0
char2_ne_zero = input('При делении % на 10 получается число отличное от 0?(да/нет): ')
if char2_ne_zero =='да':
    odd_or_not2 = input('Число, полученное при делении % на 10 делится на 2 без остатка?(да/нет): ')
    if odd_or_not2 =='да':
        char_num2 = input('Первая цифра числа больше 5?(да/нет): ')
        if char_num2 == 'да':
            cratnost_3_2 = input('Первая цифра числа кратна 3?(да/нет): ')
            if cratnost_3_2 == 'да':
                num2 = 6
            else:
                num2 = 8
        else:
            cratnost_4_2 = input('Первая цифра числа кратна 4?(да/нет): ')
            if cratnost_4_2 == 'да':
                num2 = 4
            else:
                num2 = 2
    else:
        char_num2 = input('Вторая цифра числа больше 5?(да/нет): ')
        if char_num2 == 'да':
            cratnost_3_2 = input('Вторая цифра числа кратна 3?(да/нет): ')
            if cratnost_3_2 == 'да':
                num2 = 9
            else:
                num2 = 7
        else:
            cratnost_3_2_ = input('Вторая цифра числа кратна 4?(да/нет): ')
            if cratnost_3_2_ == 'да':
                num2 = 3
            else:
                num2 = 1
else:
    num2 = 0

if num1 != 0:
    result = int(str(num1) + str(num2))
else:
    result = int(num2)
print(result)





