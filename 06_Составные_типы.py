tplNameOfType = ['List', 'Tuple', 'Set', 'Dictionary', 'String']
print('Выберите тип данных:')

for i in range(len(tplNameOfType)):
    print(str(i) + ' - ' + tplNameOfType[i])

blnKl = True
while blnKl:
    print('Введите число от 0 до ' + str(len(tplNameOfType)-1))
    intType = input()
    if intType.isdigit():
        intType = int(intType)
        if intType>=0 and intType<len(tplNameOfType):
            blnKl = False

print('Вы выбрали тип - ', tplNameOfType[intType])
print('*' * 100)

N = (len('КисленкоДенис') % 5 + 2) * 2

if intType == 0:
    # работа с типом List

    # генерирование типа List 1 вариант
    GenType1 = []
    for i in range(N):
        GenType1.append(i)
    print('Задание 1, вариант 1 ')
    print(GenType1)

    # генерирование типа List 2 вариант
    GenType1 = [i for i in range(N)]
    print('Задание 1, вариант 2 ')
    print(GenType1)

    print('*' * 100)

    # дублирование значений задание 2 вариант 1
    GenType2 = []
    for i in range(len(GenType1) * 2):
        if i < len(GenType1):
            GenType2.append(GenType1[i])
        else:
            GenType2.append(GenType1[i - len(GenType1)] + 1)

    print('Задание 2, вариант 1 ')
    print(GenType2)

    # дублирование значений задание 2 вариант 2
    GenType2 = GenType1 + [GenType1[i] + 1 for i in range(len(GenType1))]
    print('Задание 2, вариант 2 ')
    print(GenType2)

    # дублирование значений задание 2 вариант 3
    GenType2 = [GenType1[i] if i < len(GenType1) else GenType1[i - len(GenType1)] + 1 for i in range(len(GenType1) * 2)]
    print('Задание 2, вариант 3 ')
    print(GenType2)

    # дублирование значений задание 2 вариант 4
    GenType2 = [j if i < len(GenType1) else j + 1 for i, j in enumerate(GenType1 + GenType1)]
    print('Задание 2, вариант 4 ')
    print(GenType2)

    print('*' * 100)

    # выбор второго по убыванию числа задание 3 вариант 1
    print('Задание 3, вариант 1')
    print(GenType2[GenType2.index(list(set(sorted(GenType2)))[-2])])

    # выбор второго по убыванию числа задание 3 вариант 2
    print('Задание 3, вариант 2')
    GenType2.sort()
    print(GenType2[GenType2.index(list(set(GenType2))[-2])])

    print('*' * 100)

    # выбор значений индексы которых при делении на 3 дают в остатке 1 задание 4 вариант 1
    print('Задание 4 вариант 1')
    for i in range(len(GenType2)):
        if i % 3 == 1:
            print(GenType2[i], end=' ')
    print('')

    # выбор значений индексы которых при делении на 3 дают в остатке 1 задание 4 вариант 2
    print('Задание 4 вариант 2')
    for i in range(1, len(GenType2), 3):
        print(GenType2[i], end=' ')
    print('')

    # выбор значений индексы которых при делении на 3 дают в остатке 1 задание 4 вариант 3
    print('Задание 4 вариант 3')
    print([GenType2[i] for i in range(len(GenType2)) if i % 3 == 1])

    # выбор значений индексы которых при делении на 3 дают в остатке 1 задание 4 вариант 4
    print('Задание 4 вариант 4')
    print([j for i, j in enumerate(GenType2) if i % 3 == 1])

    # выбор значений индексы которых при делении на 3 дают в остатке 1 задание 4 вариант 5
    print('Задание 4 вариант 5')
    print([GenType2[i] for i in range(1, len(GenType2), 3)])

    # выбор значений индексы которых при делении на 3 дают в остатке 1 задание 4 вариант 6
    print('Задание 4 вариант 6')
    print(GenType2[1::3])

    print('*' * 100)

    # Задание 5
    intTr = int(round(len(GenType2) / 3, 0))
    intNomTr = 2
    print('Задание 5 вариант 1')
    print(GenType2)
    print(GenType2[(intNomTr - 1) * intTr:intNomTr * intTr])

    print('*' * 100)
elif intType == 1:
    # работа с типом Tuple

    # генерирование типа Tuple 1 вариант
    GenType1 = []
    for i in range(N):
        GenType1.append(i)
    GenType1 = tuple(GenType1)
    print('Задание 1, вариант 1 ')
    print(GenType1)

    # генерирование типа Tuple 2 вариант
    GenType1 = tuple([i for i in range(N)])
    print('Задание 1, вариант 2 ')
    print(GenType1)

    print('*' * 100)

    # дублирование значений задание 2 вариант 1
    GenType2 = []
    for i in range(len(GenType1) * 2):
        if i < len(GenType1):
            GenType2.append(GenType1[i])
        else:
            GenType2.append(GenType1[i - len(GenType1)] + 1)
    print('Задание 2, вариант 1 ')
    GenType2 = tuple(GenType2)
    print(GenType2)

    # дублирование значений задание 2 вариант 2
    GenType2 = tuple(list(GenType1) + [GenType1[i] + 1 for i in range(len(GenType1))])
    print('Задание 2, вариант 2 ')
    print(GenType2)

    # дублирование значений задание 2 вариант 3
    GenType2 = tuple([GenType1[i] if i < len(GenType1) else GenType1[i - len(GenType1)] + 1 for i in range(len(GenType1) * 2)])
    print('Задание 2, вариант 3 ')
    print(GenType2)

    # дублирование значений задание 2 вариант 4
    GenType2 = tuple([j if i < len(GenType1) else j + 1 for i, j in enumerate(list(GenType1) + list(GenType1))])
    print('Задание 2, вариант 4 ')
    print(GenType2)

    print('*' * 100)

    # выбор второго по убыванию числа задание 3 вариант 1
    print('Задание 3, вариант 1')
    print(GenType2[GenType2.index(list(set(sorted(list(GenType2))))[-2])])

    # выбор второго по убыванию числа задание 3 вариант 2
    print('Задание 3, вариант 2')
    TempList = list(GenType2)
    TempList.sort()
    GenType2 = tuple(set(TempList))
    print(GenType2[GenType2.index(GenType2[-2])])

    print('*' * 100)

    #выбор значений индексы которых при делении на 3 дают в остатке 1 задание 4 вариант 1
    print('Задание 4 вариант 1')
    for i in range(len(GenType2)):
        if i % 3 == 1:
            print(GenType2[i], end=' ')
    print('')

    # выбор значений индексы которых при делении на 3 дают в остатке 1 задание 4 вариант 2
    print('Задание 4 вариант 2')
    for i in range(1, len(GenType2), 3):
        print(GenType2[i], end=' ')
    print('')

    # выбор значений индексы которых при делении на 3 дают в остатке 1 задание 4 вариант 3
    print('Задание 4 вариант 3')
    print([GenType2[i] for i in range(len(GenType2)) if i % 3 == 1])

    # выбор значений индексы которых при делении на 3 дают в остатке 1 задание 4 вариант 4
    print('Задание 4 вариант 4')
    print([j for i, j in enumerate(GenType2) if i % 3 == 1])

    # выбор значений индексы которых при делении на 3 дают в остатке 1 задание 4 вариант 5
    print('Задание 4 вариант 5')
    print([GenType2[i] for i in range(1, len(GenType2), 3)])

    # выбор значений индексы которых при делении на 3 дают в остатке 1 задание 4 вариант 6
    print('Задание 4 вариант 6')
    print(GenType2[1::3])

    print('*' * 100)

    # Задание 5
    intTr = int(round(len(GenType2) / 3, 0))
    intNomTr = 2
    print('Задание 5 вариант 1')
    print(GenType2)
    print(GenType2[(intNomTr - 1) * intTr:intNomTr * intTr])

    print('*' * 100)
elif intType == 2:
    # работа с типом Set

    # генерирование типа Set 1 вариант 1
    GenType1 = []
    for i in range(N):
        GenType1.append(i)
    GenType1 = set(GenType1)
    print('Задание 1, вариант 1 ')
    print(GenType1)

    # генерирование типа Set 2 вариант 2
    GenType1 = {i for i in range(N)}
    print('Задание 1, вариант 2 ')
    print(GenType1)

    print('*' * 100)

    # дублирование значений задание 2 вариант 1
    GenType2 = []
    for i in range(len(GenType1) * 2):
        if i < len(GenType1):
            GenType2.append(list(GenType1)[i])
        else:
            GenType2.append(list(GenType1)[i - len(GenType1)] + 1)
    GenType2 = set(GenType2)

    print('Задание 2, вариант 1 ')
    print(GenType2)

    # дублирование значений задание 2 вариант 2
    GenTmp = list(GenType1)
    GenType2 = set(GenTmp + [GenTmp[i] + 1 for i in range(len(GenTmp))])
    print('Задание 2, вариант 2 ')
    print(GenType2)

    # дублирование значений задание 2 вариант 3
    GenTmp = list(GenType1)
    GenType2 = set([GenTmp[i] if i < len(GenTmp) else GenTmp[i - len(GenTmp)] + 1 for i in range(len(GenTmp) * 2)])
    print('Задание 2, вариант 3 ')
    print(GenType2)

    # дублирование значений задание 2 вариант 4
    GenType2 = set([j if i < len(GenType1) else j + 1 for i, j in enumerate(list(GenType1) + list(GenType1))])
    print('Задание 2, вариант 4 ')
    print(GenType2)

    print('*' * 100)

    # выбор второго по убыванию числа задание 3 вариант 1
    print('Задание 3, вариант 1')
    GenTmp = list(GenType2)
    print(GenTmp[GenTmp.index(sorted(GenTmp)[-2])])

    # выбор второго по убыванию числа задание 3 вариант 2
    print('Задание 3, вариант 2')
    GenTmp = list(GenType2)
    GenTmp.sort()
    print(GenTmp[GenTmp.index(GenTmp[-2])])

    print('*' * 100)

    # выбор значений индексы которых при делении на 3 дают в остатке 1 задание 4 вариант 1
    print('Задание 4 вариант 1')
    GenTmp = list(GenType2)
    for i in range(len(GenTmp)):
        if i % 3 == 1:
            print(GenTmp[i], end=' ')
    print('')

    # выбор значений индексы которых при делении на 3 дают в остатке 1 задание 4 вариант 2
    print('Задание 4 вариант 2')
    GenTmp = list(GenType2)
    for i in range(1, len(GenTmp), 3):
        print(GenTmp[i], end=' ')
    print('')

    # выбор значений индексы которых при делении на 3 дают в остатке 1 задание 4 вариант 3
    print('Задание 4 вариант 3')
    GenTmp = list(GenType2)
    print(set([GenTmp[i] for i in range(len(GenTmp)) if i % 3 == 1]))

    # выбор значений индексы которых при делении на 3 дают в остатке 1 задание 4 вариант 4
    print('Задание 4 вариант 4')
    print(set([j for i, j in enumerate(GenType2) if i % 3 == 1]))

    # выбор значений индексы которых при делении на 3 дают в остатке 1 задание 4 вариант 5
    print('Задание 4 вариант 5')
    GenTmp = list(GenType2)
    print(set([GenTmp[i] for i in range(1, len(GenTmp), 3)]))

    # выбор значений индексы которых при делении на 3 дают в остатке 1 задание 4 вариант 6
    print('Задание 4 вариант 6')
    GenTmp = list(GenType2)
    print(set(GenTmp[1::3]))

    print('*' * 100)

    # Задание 5
    intTr = int(round(len(GenType2) / 3, 0))
    intNomTr = 2
    print('Задание 5 вариант 1')
    print(GenType2)
    GenTmp = list(GenType2)
    print(GenTmp[(intNomTr - 1) * intTr:intNomTr * intTr])

    print('*' * 100)
elif intType == 3:
    # работа с типом Dictionary

    # генерирование типа Dictionary 1 вариант
    GenType1 = {}
    for i in range(N):
        GenType1[i] = i
    print('Задание 1, вариант 1 ')
    print(GenType1)

    # генерирование типа Dictionary 2 вариант
    GenType1 = {i: i for i in range(N)}
    print('Задание 1, вариант 2 ')
    print(GenType1)

    print('*' * 100)

    # дублирование значений задание 2 вариант 1
    GenType2 = {}
    intKol = 0
    for i in (list(GenType1.keys()) + list(GenType1.keys())):
        if intKol < len(GenType1):
            GenType2[i] = GenType1[i]
        else:
            GenType2[i+100] = GenType1[i] + 1
        intKol = intKol + 1

    print('Задание 2, вариант 1 ')
    print(GenType2)

    # дублирование значений задание 2 вариант 2
    GenTmp = list(GenType1.keys()) + [i + 100 for i in list(GenType1.keys())]
    GenType2 = {GenTmp[i]: GenType1[i] if i < len(GenType1) else GenType1[i-len(GenType1)] + 1 \
                                     for i in range(len(GenTmp))}
    print('Задание 2, вариант 2 ')
    print(GenType2)

    # дублирование значений задание 2 вариант 3
    GenTmp1 = list(GenType1.keys()) + [i + 100 for i in list(GenType1.keys())]
    GenTmp2 = list(GenType1.values()) + [i + 1 for i in list(GenType1.values())]
    GenType2 = {i: j for i, j in zip(GenTmp1, GenTmp2)}
    print('Задание 2, вариант 3 ')
    print(GenType2)

    print('*' * 100)

    # выбор второго по убыванию числа задание 3 вариант 1
    print('Задание 3, вариант 1')
    GenTmp = list(GenType2.values())
    print(GenTmp[GenTmp.index(list(set(sorted(GenTmp)))[-2])])

    # print('*' * 100)

    # выбор значений индексы которых при делении на 3 дают в остатке 1 задание 4 вариант 1
    print('Задание 4 вариант 1')
    GenTmp = list(GenType2.keys())
    for i in GenTmp:
        if i % 3 == 1:
            print(GenType2[i], end=' ')
    print('')

    # выбор значений индексы которых при делении на 3 дают в остатке 1 задание 4 вариант 2
    print('Задание 4 вариант 2')
    GenTmp = list(GenType2.keys())
    print([GenType2[i] for i in GenTmp if i % 3 == 1])

    # выбор значений индексы которых при делении на 3 дают в остатке 1 задание 4 вариант 3
    print('Задание 4 вариант 3')
    print([j for i, j in GenType2.items() if i % 3 == 1])

    print('*' * 100)

    # Задание 5
    GenTmp = list(GenType2.keys())
    intTr = int(round(len(GenTmp) / 3, 0))
    intNomTr = 2
    print('Задание 5 вариант 1')
    print(GenType2)
    for i in range((intNomTr-1)*intTr, intNomTr*intTr):
        print(GenType2[GenTmp[i]], end=', ')
    print('')

    print('*' * 100)
elif intType == 4:
    # работа с типом String

    # генерирование типа String 1 вариант
    GenType1 = ''
    for i in range(N):
        GenType1 = GenType1 + str(i) + ' '
    print('Задание 1, вариант 1 ')
    GenType1 = GenType1.strip()
    print(GenType1)

    # генерирование типа String 2 вариант
    GenType1 = ''.join([str(i) + ' ' for i in range(N)])
    print('Задание 1, вариант 2 ')
    GenType1 = GenType1.strip()
    print(GenType1)

    print('*' * 100)

    # дублирование значений задание 2 вариант 1
    GenType2 = ''
    GenTmp = GenType1.split(sep=' ')
    for i in range(len(GenTmp) * 2):
        if i < len(GenTmp):
            GenType2 = GenType2 + GenTmp[i] + ' '
        else:
            GenType2 = GenType2 + str(int(GenTmp[i - len(GenTmp)]) + 1) + ' '

    print('Задание 2, вариант 1 ')
    GenType2 = GenType2.strip()
    print(GenType2)

    # дублирование значений задание 2 вариант 2
    GenTmp = GenType1.split(sep=' ')
    GenType2 = GenType1 + ' ' + ''.join([str(int(GenTmp[i]) + 1) + ' ' for i in range(len(GenTmp))])
    print('Задание 2, вариант 2 ')
    GenType2 = GenType2.strip()
    print(GenType2)

    # дублирование значений задание 2 вариант 3
    GenTmp = GenType1.split(sep=' ')
    GenType2 = ''.join([GenTmp[i] + ' ' if i < len(GenTmp) else str(int(GenTmp[i - len(GenTmp)]) + 1) + ' ' for i in range(len(GenTmp) * 2)])
    print('Задание 2, вариант 3 ')
    GenType2 = GenType2.strip()
    print(GenType2)

    # дублирование значений задание 2 вариант 4
    GenTmp = GenType1.split(sep=' ')
    GenType2 = ''.join([j + ' ' if i < len(GenTmp) else str(int(j) + 1) + ' ' for i, j in enumerate(GenTmp + GenTmp)])
    print('Задание 2, вариант 4 ')
    GenType2 = GenType2.strip()
    print(GenType2)

    print('*' * 100)

    # выбор второго по убыванию числа задание 3 вариант 1
    print('Задание 3, вариант 1')
    GenTmp = [int(i) for i in GenType2.split(sep=' ')]
    print(GenTmp[GenTmp.index(list(set(sorted(GenTmp)))[-2])])

    # выбор второго по убыванию числа задание 3 вариант 2
    print('Задание 3, вариант 2')
    GenTmp = [int(i) for i in GenType2.split(sep=' ')]
    GenTmp.sort()
    print(GenTmp[GenTmp.index(list(set(GenTmp))[-2])])

    print('*' * 100)

    # выбор значений индексы которых при делении на 3 дают в остатке 1 задание 4 вариант 1
    print('Задание 4 вариант 1')
    GenTmp = [int(i) for i in GenType2.split(sep=' ')]
    for i in range(len(GenTmp)):
        if i % 3 == 1:
            print(GenTmp[i], end=' ')
    print('')

    # выбор значений индексы которых при делении на 3 дают в остатке 1 задание 4 вариант 2
    print('Задание 4 вариант 2')
    GenTmp = [int(i) for i in GenType2.split(sep=' ')]
    for i in range(1, len(GenTmp), 3):
        print(GenTmp[i], end=' ')
    print('')

    # выбор значений индексы которых при делении на 3 дают в остатке 1 задание 4 вариант 3
    print('Задание 4 вариант 3')
    GenTmp = [int(i) for i in GenType2.split(sep=' ')]
    print([GenTmp[i] for i in range(len(GenTmp)) if i % 3 == 1])

    # выбор значений индексы которых при делении на 3 дают в остатке 1 задание 4 вариант 4
    print('Задание 4 вариант 4')
    GenTmp = [int(i) for i in GenType2.split(sep=' ')]
    print([j for i, j in enumerate(GenTmp) if i % 3 == 1])

    # выбор значений индексы которых при делении на 3 дают в остатке 1 задание 4 вариант 5
    print('Задание 4 вариант 5')
    GenTmp = [int(i) for i in GenType2.split(sep=' ')]
    print([GenTmp[i] for i in range(1, len(GenTmp), 3)])

    # выбор значений индексы которых при делении на 3 дают в остатке 1 задание 4 вариант 6
    print('Задание 4 вариант 6')
    GenTmp = [int(i) for i in GenType2.split(sep=' ')]
    print(GenTmp[1::3])
    print('*' * 100)

    # Задание 5
    GenTmp = [int(i) for i in GenType2.split(sep=' ')]
    intTr = int(round(len(GenTmp) / 3, 0))
    intNomTr = 2
    print('Задание 5 вариант 1')
    print(GenType2)
    print(GenTmp[(intNomTr - 1) * intTr:intNomTr * intTr])

    print('*' * 100)
