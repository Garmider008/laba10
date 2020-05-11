''' Сформувати функцію для обчислення індексу максимального елемента масиву
n*n, де 1<=n<=5.
Гармідер Анастасія'''

from random import randint
import numpy as np
import timeit
def X(z):#функція для перевірки
    t_max = 0
    w_max = 0
    max1 = 0 #максмальний елемент
    for c in range(len(z)):
        for d in range(len(z)):
            if z[c][d] > z[t_max][w_max]:
                max1 = z[c][d]
                t_max = c
                w_max = d
    return (f'Max:{max1} on {t_max+1},{w_max+1}')
n = int(input('Введіть число:'))
if 1 <= n <= 5: #створюємо масив
    m = n
    a = np.zeros((n,m),dtype=int)
    for h in range(n):
        for q in range(m):
            a[h][q] = randint(1,40)
    print('Індекс максимального елемента масиву:')
    print(X(a))
t = timeit.timeit('"-".join(str(n) for n in range(100))', number=9999)
print(f'Програма працювала {t} секунд')

''''-------------------------------------------------------------------------'''''

def A(b, c = 0, d = 0, c_max = 0, d_max = 0, max = 0): #функція для перевірки
    if d == len(b[c]):
        c += 1  #рядочок
        d = 0  #стовбець
    if c == len(b):
        return c_max, d_max
    if b[c][d] > b[c_max][d_max]:
        max = b[c][d]
        c_max = c
        d_max = d
    d += 1
    return A(b, c, d, c_max, d_max)
r = int(input('Введіть число:'))
if 1 <= r <= 5: #масив
    m = r
    b = np.zeros((r, m), dtype = int)
    for c in range(r):
        for d in range (m):
            b[c][d] = randint(1, 40)
    print('Індекс максимального елемента масиву:')
    print(A(b))
t = timeit.timeit('"-".join(str(n) for n in range(100))', number = 9999)
print(f'Програма працювала {t} секунд')

'''Другий код зайняв приблизно пів дня написання, а ось перший приблизно за 2 години. Читабельність краща також у 1'''
'''у цій програмі рекурсія працює швидше ніж ітерація, а ось пам'ять займають однаково'''