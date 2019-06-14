# Задание 1

import random as rnd


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


def partn(num_x, vsego_h, tek_hod):
    kolendpart = 0
    while tek_hod <= vsego_h:
        tek_hod += 1
        intNumP = vvod_p_n()
        if intNumP < num_x:
            print('Ваше число меньше загаданного!!!')
        elif intNumP > num_x:
            print('Ваше число больше загаданного!!!')
        else:
            print('Да, это оно!!!')
            kolendpart = 1
            break
        print('')
    return kolendpart, tek_hod


rnd.seed()
intKolEndPart = 0
intVsegoPart = 0
intVsegoH = 50
intTekHod = 0
blnKl = True

while blnKl:
    intNumX = rnd.randint(1, 100)
    intKolEndPartT, intTekHodT = partn(intNumX, intVsegoH, intTekHod)
    intKolEndPart += intKolEndPartT
    intTekHod = intTekHodT
    intVsegoPart += 1
    if intTekHod >= intVsegoH:
        break

    print('Хотите сыграть еще? (y/n) ', end='')
    chOtv = input()
    if chOtv != 'y':
        blnKl = False

print('Всего партий - ' + str(intVsegoPart))
print('Всего оконченных партий - ' + str(intKolEndPart))

#***************************************************
