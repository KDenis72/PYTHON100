# Задание 1
def kol_day(intKolKM):
    intKolDay = 0
    intDist = 0
    while intDist < intKolKM:
        intKolDay += 1
        intDist += 2 ** intKolDay

    return intKolDay


# print('За ' + str(kol_day(1000)) + ' я пробегу 1000 км.')
# print('За ' + str(kol_day(10000)) + ' я пробегу 10000 км.')
# ________________________________________

# Задание 2
def prost_number(intPred: int):
    intSl = intPred + 1
    blnKl = True

    while blnKl:
        blnKl = False
        for i in range(2, intSl // 2 + 1):
            if intSl % i == 0:
                blnKl = True
                intSl += 1
                break

    return intSl

## Первый вариант
def days_of_km(fltDistKM: float):
    intDay = 0
    fltSSSDist = 0
    intPNumber = 1

    while fltSSSDist <= fltDistKM:
        intPNumber = prost_number(intPNumber)
        fltSSSDist += intPNumber
        intDay += 1

    return intDay


print('Спортсмен пробежит 1000 км за ' + str(days_of_km(1000)) + ' дней')
print('Спортсмен пробежит 10000 км за ' + str(days_of_km(10000)) + ' дней')


## Второй вариант
def days_of_km2(lstProstNum1: list, fltDistKM: float):
    intDay = 0
    fltSSSDist = 0

    while fltSSSDist <= fltDistKM:
        fltSSSDist += lstProstNum1[intDay]
        intDay += 1

    return intDay


lstProstNum = sorted(list({prost_number(i) for i in range(1, 10000)}))

print('Спортсмен пробежит 1000 км за ' + str(days_of_km2(lstProstNum, 1000)) + ' дней')
print('Спортсмен пробежит 10000 км за ' + str(days_of_km2(lstProstNum, 10000)) + ' дней')
# _________________________________________

# Задание 3
def kol_km(intStKM = 10, fltProc = 10, intKolDay = 30):
    intSummDay = 1
    fltDist = intStKM
    fltDayDist = intStKM

    while intSummDay <= intKolDay:
        intSummDay += 1
        fltDayDist = fltDayDist if intSummDay % 2 != 0 else fltDayDist * (1 + fltProc / 100)
        fltDist += fltDayDist

    return fltDist


#print('за 30 дней спортсмен пробежит - ' + str(kol_km(10, 15, 30)) + ' км')
# _________________________________________

# Задание 4
import math


def kol_day2(fltStDist = 10, fltProc = 10, fltSummDist = 100, fltDayDist = 20):
    def kol_day_of_km(fltDistNach, fltDistOfDay, fltProc):
        return math.ceil(math.log(fltDistOfDay/fltDistNach, (1 + fltProc / 100)) + 1)


    def kol_km_of_day(fltDistNach, intDay, fltProc):
        return fltDistNach * (1 + fltProc / 100) ** (intDay - 1)


    intSummKolDay = 1
    fltSSSDist = fltStDist

    while fltSSSDist < fltSummDist:
        intSummKolDay += 1
        fltSSSDist += kol_km_of_day(fltStDist, intSummKolDay, fltProc)

    return kol_day_of_km(fltStDist, fltDayDist, fltProc), intSummKolDay

intKolKMofDay, intKolSummKM = kol_day2(10, 10, 100, 20)
# print('Спортсмен будет пробегать больше 20 км в день на ' + str(intKolKMofDay) + ' день')
# print('Спортсмен пробежит суммарно 100 км на ' + str(intKolSummKM) + ' день')
# _________________________________________

