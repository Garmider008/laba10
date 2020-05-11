'''Сформувати функцію, що буде обчислювати факторіал заданого користувачем
натурального числа n через рекурсію
Гармідер Анастасія 122В'''
import timeit
def b(a): #створюємо цикл для виведення на кожному етапі
    if a == 0:
        return 1
    else:
        return b (a-1) * a # тобто сама через себе
c = int(input('Введіть число:'))
print('Факторіал вашого числа:')
print(b (c))
t = timeit.timeit('"-".join(str(n) for n in range(100))', number=9999)
print(f'Програма працювала {t} секунд')

''''-------------------------------------------------------------------------'''''

def d(o):#створюємо цикл для виведення на кожному етапі
    v = 1 #лічильник
    while o > 1:
        v *= o #рекурсія
        o -= 1
    return v
k = int(input('Введіть число:'))
print('Факторіал вашого числа:')
print(d(k))
t = timeit.timeit('"-".join(str(n) for n in range(100))', number=9999)
print(f'Програма працювала {t} секунд')

'''Написання першої програми зайняло на 15 хвилин менше, також читабельність першої програми краща. 
І по струкруті 1 програма менша ніж 2 '''