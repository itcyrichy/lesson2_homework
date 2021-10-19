# for
for i in range(10):
    print(i)
    if i == 5: break

for i in range(10):
    answer = input('Какая лучшая марка автомобиля?')
    if answer == 'Volvo':
        print('Вы абсолютно правы!')
        break

for i in range(10):
    if i == 9: break
    if i < 3: continue
    else:    print(i)

# if
brand = 'Volvo'
engine_volume = 1.5
horsepower = 152
sunroof = True

if horsepower < 80:
    print('No Tax')

if horsepower < 80:
    print('No Tax')
else:
    print('Tax')

tax = 0
if horsepower < 80:
    tax = 0
elif horsepower < 100:
    tax = 10000
elif horsepower < 150:
    tax = 20000
else:
    tax = 50000
print(tax)



cool_car = 0

cool_car = 1 if sunroof == 1 else 0

print(cool_car)


# input_output

print('Hello!')
print('Hello!', 'Student!', 123)

print('Hello!', 'Student!', 123, sep = 'xxx')

print('Hello!', 'Student!', 123, end = 'yyy')

print()

age = input('Input your age')

print(age, type(age))
print(int(age), type(int(age)))

# math_ops
a = input('First number')
b = input('Second number')
a = int(a)
b = int(b)
print(a + b)
print(a - b)
print(a * b)
result = a / b
print(type(result))
print(result)
print(a ** 2)

# Логические операции
a = True
b = False

# Отрицание
print(not a)
# Логическое И
print(a and b)
# логическое ИЛИ
print(a or b)

a = 10
print(a > 100)
print(a < 100)
print(a <= 100)
print(a >= 100)
print(a == 100)
print(a != 100)

# type var:
name = 'Ford'

print(name, type(name))

age = 3

print(age, type(age))

engine_volume = 1.6

print(engine_volume,type(engine_volume))

see_sky = False

print(see_sky, type(see_sky))

# var id
def is_digit(string):
    if string.isdigit():
       return True
    else:
        try:
            float(string)
            return True
        except ValueError:
            return False

temp_var_1 = input('Input something!')

print(temp_var_1, type(temp_var_1), id(temp_var_1))

temp_var_2 = input('Input something again!')

print(temp_var_2, type(temp_var_2), id(temp_var_2))

temp_var_1 = int(temp_var_2)

print(temp_var_1, type(temp_var_1), id(temp_var_1))

temp_float = input('Input float number!')
print(temp_float, type(temp_float), id(temp_float))

if is_digit(temp_float):
    temp_float = float(temp_float)
    print(temp_float, type(temp_float), id(temp_float))
else: print('There is not number!')

# while
i = 0

while i < 10:
    print(i)
    i = i + 1
    if i == 5: break



answer = None

while answer != 'Volvo':
    answer = input('Какая лучшая марка автомобиля?')
print('Вы абсолютно правы!')


while i < 10:
    if i == 9: break
    if i <3: continue
    print(i)
    i = i + 1
