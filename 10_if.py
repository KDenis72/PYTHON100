# Задание 1

import random as rnd


def initdatapart():
    return rnd.randint(1, 100), 50


def vvod_p_n():
    blnKl = True
    while blnKl:
        print('Введите целое чило от 1 до 100: ', end='')
        intNum = input()
        print()
        if intNum.isdigit():
            intNum = int(intNum)
            if intNum >= 1 and intNum <=100:
                blnKl = False

    return intNum


def partn(num_x, vsego_h):
    kolendpart = 0
    for i in range(vsego_h):
        intNumP = vvod_p_n()
        if intNumP < num_x:
            print('Ваше число меньше загаданного!!!')
        elif intNumP > num_x:
            print('Ваше число больше загаданного!!!')
        else:
            print('Да, это оно!!!')
            kolendpart = 1
            break
    return kolendpart


rnd.seed()
intKolEndPart = 0
intVsegoPart = 0
blnKl = True

while blnKl:
    intNumX, intVsegoH = initdatapart()
    intKolEndPart += partn(intNumX, intVsegoH)
    intVsegoPart += 1
    print('Хотите сыграть еще? (y/n) ', end='')
    chOtv = input()
    if chOtv != 'y':
        blnKl = False

print('Всего партий - ' + str(intVsegoPart))
print('Всего оконченных партий - ' + str(intKolEndPart))

#***************************************************
