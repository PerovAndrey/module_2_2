# name = input('Введите Ваше имя: ')
# if name == 'Urban':
#     print('Здравствуйте, администратор')
# if name == 'Andrei':
#     print('Здравствуйте, студент')
# else:
#     print('Привет', name)
# number = int(input('Введите число')) # Fizz, Buzz, FizzBuzz
# if number % 3 == 0 and number % 5 == 0:
#     print('FizzBuzz')
# elif number % 3 == 0:
#     print('Fizz')
# elif number % 5 == 0:
#     print('Buzz')
# else:
#     print('Число не подходит')

first = int(input('Введите число'))
second = int(input('Введите второе число'))
third = int(input('Введите третье число'))
if first == second == third:
    print('3')
elif first == second and second != third or first != second and second == third or first == third and first != second:
    print('2')
elif first != second != third:
    print('0')