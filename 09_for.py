# Задание 1 вариант 1
def init_lst(nn1, n1):
    lstPos1 = [1 for _ in range(nn1)]

    for i in range(nn1, n1):
        ss = 0
        for j in range(i - nn1, i):
            ss += lstPos1[j]
        lstPos1.append(ss)

    return lstPos1


# Задание 1 вариант 1_1
def init_lst1(nn1, n1):
    lstPos1 = [1 for _ in range(nn1)]

    for _ in range(n1 - nn1):
        ss = 0
        for j in range(-nn1, 0):
            ss += lstPos1[j]
        lstPos1.append(ss)

    return lstPos1


# Задание 1 вариант 1_2
def init_lst2(nn1, n1):
    lstPos1 = [1 for _ in range(nn1)]

    for _ in range(n1 - nn1):
        lstPos1.append(sum(lstPos1[-nn1:]))

    return lstPos1


# print('Введите NN: ', end='')
# nn = int(input())
# print('')
# print('Введите номер элемента последовательности: ', end='')
# n = int(input())
# print('')
# lstPos = init_lst2(nn, n)
#
# print(lstPos[n-1])
# _____________________________

# Задание 1 вариант 2 и 3
def n_element(n1):
    x1 = 1
    x2 = 1
    xn = 1

    for i in range(3, n1 + 1):
        xn = x1 + x2
        x1, x2 = x2, xn

    return xn

#print('Введите номер элемента последовательности: ', end='')
#n = int(input())
#print('')
# Вариант 2
#print(n_element(n))

# Вариант 3
#print([n_element(i) for i in range(1, n + 1)][n - 1])
# _____________________________

# Задание 2 вариант 1
def init_lst2(n1):
    lstPos1 = [0 if i > 2 else 1 for i in range(n1)]

    for i in range(3, n1):
        lstPos1[i] = lstPos1[i - 3] + lstPos1[i - 2] + lstPos1[i - 1]

    return lstPos1


# print('Введите номер элемента последовательности: ', end='')
# n = int(input())
# print('')
# lstPos = init_lst2(n)
#
# print(lstPos[n-1])
# _____________________________

# Задание 1 вариант 2 и 3
def n_element2(n1):
    x1 = 1
    x2 = 1
    x3 = 1
    xn = 1

    for i in range(4, n1 + 1):
        xn = x1 + x2 + x3
        x1, x2, x3 = x2, x3, xn

    return xn

# print('Введите номер элемента последовательности: ', end='')
# n = int(input())
# print('')
# # Вариант 2
# print(n_element2(n))
#
# # Вариант 3
# print([n_element2(i) for i in range(1, n + 1)][n - 1])
# _____________________________

# Задание 3 вариант 1
def kv_nech_num(n1):
    return [i ** 2 for i in range(1, n1 + 1, 2)]


# print('Введите N: ', end='')
# n = int(input())
# print('')
# print(kv_nech_num(n))

# Задание 3 вариант 2
def kv_nech_num2(n1):
    lstL = []
    for i in range(1, n1 + 1, 2):
        lstL.append(i ** 2)

    return lstL


# print('Введите N: ', end='')
# n = int(input())
# print('')
# print(kv_nech_num2(n))

# Задание 4 вариант 1
def paint_kv(a1, b1, d1, ch1='*'):
    s1 = ch1 * a1 + '\n'

    if d1 >= b1:
        s = s1 * b1
    else:
        s = ''
        for _ in range(d1):
            s += s1

        for _ in range(b1 - d1 * 2):
            if d1 >= a1:
                s += s1
            else:
                s += ch1 * d1 + ' ' * (a1 - 2 * d1) + ch1 * d1 + '\n'

        for _ in range(d1):
            s += s1

    return s


# Задание 4 вариант 2
def paint_kv2(a1, b1, d1, ch1='*'):
    s1 = ch1 * a1 + '\n'

    if d1 >= b1 or d1 >= a1:
        s = s1 * b1
    else:
        s = s1 * d1

        s += (ch1 * d1 + ' ' * (a1 - 2 * d1) + ch1 * d1 + '\n') * (b1 - d1 * 2)

        s += s1 * d1

    return s


# print('Введите A: ', end='')
# a = int(input())
# print('')
#
# print('Введите B: ', end='')
# b = int(input())
# print('')
#
# print('Введите D: ', end='')
# d = int(input())
# print('')
#
# print(paint_kv2(a, b, d, '*'))

# Задание 5
def s_nat(a1, b1):
    intSumm = 0
    intMult = 1
    for i in range(a1, b1 + 1):
        intSumm += i
        intMult *= i

    return intSumm, intMult


# print('Введите A: ', end='')
# a = int(input())
# print('')
#
# print('Введите B: ', end='')
# b = int(input())
# print('')
#
# intS, intM = s_nat(a, b)
# print('Сумма - ' + str(intS) + ' произведение - ' + str(intM))

# Задание 6 вариант 1
def chet_nechet(a1, b1):
    lstNech = []
    lstChet = []
    for i in range(a1 + 1, b1):
        if i % 2 == 0:
            lstChet.append(i)
        else:
            lstNech.append(i)

    return lstChet, lstNech


# print('Введите A: ', end='')
# a = int(input())
# print('')
#
# print('Введите B: ', end='')
# b = int(input())
# print('')
#
# lstC, lstN = chet_nechet(a, b)
# print(f'Список четных чисел {lstC}, список нечетных чисел {lstN}')


# Задание 6 вариант 2
def chet_nechet2(a1, b1):
    return [i for i in range(a1 + 1, b1) if i % 2 == 0], [i for i in range(a1 + 1, b1) if i % 2 != 0]


# print('Введите A: ', end='')
# a = int(input())
# print('')
#
# print('Введите B: ', end='')
# b = int(input())
# print('')
#
# lstC, lstN = chet_nechet2(a, b)
# print(f'Список четных чисел {lstC}, список нечетных чисел {lstN}')

# Задание 7 вариант 1
def pol_otr(lstIsh1):
    lstPol = []
    lstOtr = []
    for i in lstIsh1:
        if i < 0:
            lstOtr.append(i)
        else:
            lstPol.append(i)

    return lstPol, lstOtr

# Генерация исходного списка
import random

random.seed()
n = random.randint(2, 100)
lstIsh = [random.random() * 100 * (-1) ** int(random.randint(1, 100)) for _ in range(n)]
# print(lstIsh)

lstP, lstO = pol_otr(lstIsh)
# print(f'Список положительных чисел {lstP}, список отрицательных чисел {lstO}')


# Задание 7 вариант 2
def pol_otr2(lstIsh1):
    return [i for i in lstIsh1 if i >= 0], [i for i in lstIsh1 if i < 0]


lstP, lstO = pol_otr(lstIsh)
# print(f'Список положительных чисел {lstP}, список отрицательных чисел {lstO}')
