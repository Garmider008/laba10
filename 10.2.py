'''Сформувати функцію для обчислення цифрового кореню натурального числа.
Цифровий корінь отримується наступним чином: необхідно скласти всі цифри заданого
числа, потім скласти всі цифри знайденої суми і повторювати процес до тих пір, поки
сума не буде дорівнювати однозначному числу, що і буде цифровим коренем заданого
числа.Рекурсивний метод
Гармідер Анастасія 122В'''

import timeit
def p(e): #функція для суми
    g = 0
    if e <= 9:
        return e
    else:
       while e > 10:
           g += e % 10
           e //= 10
           e += g
       return e
d = int(input('Введіть число:'))
print('Ваш цифровий корінь:')
print(p(d))
t = timeit.timeit('"-".join(str(n) for n in range(100))', number=9999)
print(f'Програма працювала {t} секунд')

''''-------------------------------------------------------------------------'''''

def b(a): #рекурсивна сума
    if a <= 9:
        return a
    else:
        return b (a//10) + a % 10
def c(a):#перевірка чи явлюється число однозначним
    if a <= 9:
        return a
    else:
        return c(b(a))
n = int(input('Введіть число:'))
print('Ваш цифровий корінь:')
print(c(n))
t = timeit.timeit('"-".join(str(n) for n in range(100))', number=9999)
print(f'Програма працювала {t} секунд')

'''Написання першої програми зайняло на годинку менше, за другу. Також читабельність краща у 1 ніж у 2 '''