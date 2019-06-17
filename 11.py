# Задание 1 вариант 1
def fff(a, x, b, y, s):
    strf = ''
    for i in range(a + 1):
        for j in range(b + 1):
            if (i * x + j * y) == s:
                strf += 'Нужно ' + str(i) + ' монет по ' + str(x) + ' руб и ' + str(j) + ' монет по ' + str(y) + ' рублей' + '\n'
    return strf


# Задание 1 вариант 2
def fff1(a, x, b, y, s):
    strT = []
    for i in range(a + 1):
        for j in range(b + 1):
            if (i * x + j * y) == s:
                strT.append([i, x, j, y])
    return strT


# Задание 1 вариант 3
def fff2(a, x, b, y, s):
    return [[i, x, j, y] for j in range(b + 1) for i in range(a + 1) if (i * x + j * y) == s]


intA = 5
intX = 10
intB = 6
intY = 2

intS = 50

# print(fff(intA, intX, intB, intY, intS))
#
# lstRez = fff1(intA, intX, intB, intY, intS)
# for i in lstRez:
#     print('Нужно ' + str(i[0]) + ' монет по ' + str(i[1]) + ' руб и ' + str(i[2]) + ' монет по ' + str(i[3]) + ' рублей')
#
# lstRez = fff2(intA, intX, intB, intY, intS)
# for i in lstRez:
#     print('Нужно ' + str(i[0]) + ' монет по ' + str(i[1]) + ' руб и ' + str(i[2]) + ' монет по ' + str(i[3]) + ' рублей')

# _________________________________________________________________________________________________

# Задание 2
def n_raz(kk):
    return(len(kk))


#k = input()
# print(n_raz(k))

# ______________________________________________________________________________________________

# Задание 3
def prov_str(strP):
    return 'Да' if strP[::-1] == strP else 'Нет'


# print('Введите строку -', end=' ')
# sss = input()
# print(prov_str(sss))

# _______________________________________________________________________________________________

# Задание 4
def zam_strok(strStr, strP, strZ):
    return strStr.replace(strP, strZ)


# print('Введите строку', end=' ')
# strStrok = input()
# print('Введите подстроку для замены', end=' ')
# strIsk = input()
# print('Введите подстроку на которую произвести замену', end=' ')
# strZam = input()
#
# print(zam_strok(strStrok, strIsk, strZam))

# _______________________________________________________________________________________________