import tkinter as tk
from tkinter import messagebox as msgbox
import random as rnd
import time
import math


def click_left(event):
    global canvas
    global tplKoorKvN
    global tplKoorKvK
    global blnPaintZero
    global lstDate

    if not blnEEE:
        if not blnWin:
            for i in range(len(tplKoorKvN)):
                if event.x>tplKoorKvN[i][0] and event.y>tplKoorKvN[i][1] and \
                   event.x < tplKoorKvK[i][0] and event.y < tplKoorKvK[i][1]:
                    if lstDate[i // 3][i - (i // 3) * 3] == 0:
                        if blnPaintZero:
                            blnPaintZero = not blnPaintZero
                            lstDate[i // 3][i - (i // 3) * 3] = 10
                            win_def(i)
                            paint_zero(i)
                        else:
                            blnPaintZero = not blnPaintZero
                            lstDate[i // 3][i - (i // 3) * 3] = 1
                            win_def(i)
                            paint_cross(i)

                        win_proc(i)

                    break
            if blnWin:
                msgbox.showinfo('Игра окончена!!!', ('Выиграли нолики!!!' if not blnPaintZero else 'Выиграли крестики!!!'))
        else:
            msgbox.showinfo('Игра окончена!!!', ('Выиграли нолики!!!' if not blnPaintZero else 'Выиграли крестики!!!'))
    if (not blnWin) and blnEEE:
        msgbox.showinfo('Игра окончена!!!', 'Ничья!!! Ничья!!! Ничья!!!')


def win_def(i):
    global blnEEE
    global blnWin
    global lstDate

    # Поиск по строке
    intSumm = 0
    for j in range(3):
        intSumm += lstDate[i // 3][j]
    if intSumm == 3 or intSumm == 30:
        blnWin = True

    # Поиск по столбцу
    intSumm = 0
    for j in range(3):
        intSumm += lstDate[j][i - (i // 3) * 3]
    if intSumm == 3 or intSumm == 30:
        blnWin = True

    # Поиск по диагонали
    if i == (i // 3) * 4:
        intSumm = 0
        for j in range(3):
            intSumm += lstDate[j][j]
        if intSumm == 3 or intSumm == 30:
            blnWin = True

    # Поиск по обратной диагонали
    if i == (i // 3) * 2 + 2:
        intSumm = 0
        for j in range(3):
            intSumm += lstDate[j][2 - j]
        if intSumm == 3 or intSumm == 30:
            blnWin = True

    # Определение ничьи
    blnKKK = False
    for ii in lstDate:
        for jj in ii:
            if jj == 0:
                blnKKK = True

    if (not blnKKK) and (not blnWin):
        blnEEE = True


def win_proc(i):
    global blnWin
    global lstDate
    global canvas
    global intCanvasSize
    global intDlOtr
    global blnStyleLine

    # Поиск по строке
    intSumm = 0
    for j in range(3):
        intSumm += lstDate[i // 3][j]
    if intSumm == 3 or intSumm == 30:
        blnWin = True

        if blnStyleLine:
            intN = 0
            ii = (i // 3) * (intCanvasSize // 3) + (intCanvasSize // 6)
            ij2 = ii
            while intN < intCanvasSize:
                ij1 = rnd.randint(ii - 4, ii + 4)
                canvas.create_line(intN, ij2, intN + intDlOtr, ij1, fill='red', width=5)
                time.sleep(fltTimeDelay)
                canvas.update()
                ij2 = ij1
                intN += intDlOtr
        else:
            canvas.create_line(0, (i // 3) * (intCanvasSize // 3) + (intCanvasSize // 6), intCanvasSize, (i // 3) * (intCanvasSize // 3) + (intCanvasSize // 6), fill='red', width=4)

    # Поиск по столбцу
    intSumm = 0
    for j in range(3):
        intSumm += lstDate[j][i - (i // 3) * 3]
    if intSumm == 3 or intSumm == 30:
        blnWin = True

        if blnStyleLine:
            intN = 0
            ii = (i - (i // 3) * 3) * (intCanvasSize // 3) + (intCanvasSize // 6)
            ij2 = ii
            while intN < intCanvasSize:
                ij1 = rnd.randint(ii - 4, ii + 4)
                canvas.create_line(ij2, intN, ij1, intN + intDlOtr, fill='red', width=5)
                time.sleep(fltTimeDelay)
                canvas.update()
                ij2 = ij1
                intN += intDlOtr
        else:
            canvas.create_line((i - (i // 3) * 3) * (intCanvasSize // 3) + (intCanvasSize // 6), 0, (i - (i // 3) * 3) * (intCanvasSize // 3) + (intCanvasSize // 6), intCanvasSize, fill='red', width=4)

    # Поиск по диагонали
    if i == (i // 3) * 4:
        intSumm = 0
        for j in range(3):
            intSumm += lstDate[j][j]
        if intSumm == 3 or intSumm == 30:
            blnWin = True

            if blnStyleLine:
                intN = 0
                ii = 0
                ij2 = ii
                ij4 = ii
                while intN < intCanvasSize:
                    ij1 = rnd.randint(ii - 4, ii + 4)
                    ij3 = rnd.randint(ii - 4, ii + 4)
                    canvas.create_line(intN + ij2, intN + ij4, intN + intDlOtr + ij1, intN + intDlOtr + ij3, fill='red', width=5)
                    time.sleep(fltTimeDelay)
                    canvas.update()
                    ij2 = ij1
                    ij4 = ij3
                    intN += intDlOtr
            else:
                canvas.create_line(0, 0, intCanvasSize, intCanvasSize, fill='red', width=4)

    # Поиск по обратной диагонали
    if i == (i // 3) * 2 + 2:
        intSumm = 0
        for j in range(3):
            intSumm += lstDate[j][2 - j]
        if intSumm == 3 or intSumm == 30:
            blnWin = True

            if blnStyleLine:
                intN = intCanvasSize
                intN1 = 0
                ii = 0
                ij2 = ii
                ij4 = ii
                while intN > 0:
                    ij1 = rnd.randint(ii - 4, ii + 4)
                    ij3 = rnd.randint(ii - 4, ii + 4)
                    canvas.create_line(intN - ij2, intN1 + ij4, intN - intDlOtr - ij1, intN1 + intDlOtr + ij3,  fill='red', width=5)
                    time.sleep(fltTimeDelay)
                    canvas.update()
                    ij2 = ij1
                    ij4 = ij3
                    intN -= intDlOtr
                    intN1 += intDlOtr
            else:
                canvas.create_line(0, intCanvasSize, intCanvasSize, 0, fill='red', width=4)


def paint_zero(i):
    global canvas
    global tplKoorKvN
    global tplKoorKvK
    global intCanvasSize
    global blnStyleLine
    global fltStepRad
    global fltTimeDelay

    if blnStyleLine:
        iiX = tplKoorKvN[i][0] + (tplKoorKvK[i][0] - tplKoorKvN[i][0]) // 2
        iiY = tplKoorKvN[i][1] + (tplKoorKvK[i][1] - tplKoorKvN[i][1]) // 2
        intR = (tplKoorKvK[i][0] - tplKoorKvN[i][0]) // 2 - intCanvasSize // 20
        intRad = 0.0

        ij2 = int(iiX + intR * math.cos(intRad))
        ij4 = int(iiY + intR * math.sin(intRad))
        while intRad <= 7:
            ij1 = int(rnd.uniform(iiX + intR * math.cos(intRad) - 8, iiX + intR * math.cos(intRad) + 8))
            ij3 = int(rnd.uniform(iiY + intR * math.sin(intRad) - 8, iiY + intR * math.sin(intRad) + 8))
            canvas.create_line(ij2, ij4, ij1, ij3, width=3)

            time.sleep(fltTimeDelay)
            canvas.update()
            ij2 = ij1
            ij4 = ij3
            intRad += fltStepRad
    else:
        canvas.create_oval(tplKoorKvN[i][0] + intCanvasSize // 20,
                           tplKoorKvN[i][1] + intCanvasSize // 20,
                           tplKoorKvK[i][0] - intCanvasSize // 20,
                           tplKoorKvK[i][1] - intCanvasSize // 20, width=3)


def paint_cross(i):
    global canvas
    global tplKoorKvN
    global tplKoorKvK
    global intCanvasSize
    global blnStyleLine

    if blnStyleLine:
        intN = tplKoorKvN[i][0] + intCanvasSize // 20
        intN1 = tplKoorKvN[i][1] + intCanvasSize // 20
        ii = 0
        ij2 = ii
        ij4 = ii
        while intN < tplKoorKvK[i][0] - intCanvasSize // 20:
            ij1 = rnd.randint(ii - 4, ii + 4)
            ij3 = rnd.randint(ii - 4, ii + 4)
            canvas.create_line(intN + ij2, intN1 + ij4, intN + intDlOtr + ij1, intN1 + intDlOtr + ij3, fill='black', width=3)
            time.sleep(fltTimeDelay)
            canvas.update()
            ij2 = ij1
            ij4 = ij3
            intN += intDlOtr
            intN1 += intDlOtr
    else:
        canvas.create_line(tplKoorKvN[i][0] + intCanvasSize // 20,
                           tplKoorKvN[i][1] + intCanvasSize // 20,
                           tplKoorKvK[i][0] - intCanvasSize // 20,
                           tplKoorKvK[i][1] - intCanvasSize // 20, width=3)

    if blnStyleLine:
        intN = tplKoorKvK[i][0] - intCanvasSize // 20
        intN1 = tplKoorKvN[i][1] + intCanvasSize // 20
        ii = 0
        ij2 = ii
        ij4 = ii
        while intN > tplKoorKvN[i][0] + intCanvasSize // 20:
            ij1 = rnd.randint(ii - 4, ii + 4)
            ij3 = rnd.randint(ii - 4, ii + 4)
            canvas.create_line(intN - ij2, intN1 + ij4, intN - intDlOtr - ij1, intN1 + intDlOtr + ij3, fill='black', width=3)
            time.sleep(fltTimeDelay)
            canvas.update()
            ij2 = ij1
            ij4 = ij3
            intN -= intDlOtr
            intN1 += intDlOtr
    else:
        canvas.create_line(tplKoorKvK[i][0] - intCanvasSize // 20,
                           tplKoorKvN[i][1] + intCanvasSize // 20,
                           tplKoorKvN[i][0] + intCanvasSize // 20,
                           tplKoorKvK[i][1] - intCanvasSize // 20, width=3)


def paint_cells():
    global canvas
    global intCanvasSize
    global intDlOtr
    global blnStyleLine

    if blnStyleLine:
        intN = 0
        ii = intCanvasSize // 3
        ij2 = ii
        while intN<intCanvasSize:
            ij1 = rnd.randint(ii - 4, ii + 4)
            canvas.create_line(ij2, intN, ij1, intN + intDlOtr, fill='black', width=5)
            time.sleep(fltTimeDelay)
            canvas.update()
            ij2 = ij1
            intN += intDlOtr

        intN = 0
        ii = intCanvasSize // 3 * 2
        ij2 = ii
        while intN < intCanvasSize:
            ij1 = rnd.randint(ii - 4, ii + 4)
            canvas.create_line(ij2, intN, ij1, intN + intDlOtr, fill='black', width=5)
            time.sleep(fltTimeDelay)
            canvas.update()
            ij2 = ij1
            intN += intDlOtr

        intN = 0
        ii = intCanvasSize // 3
        ij2 = ii
        while intN < intCanvasSize:
            ij1 = rnd.randint(ii - 4, ii + 4)
            canvas.create_line(intN, ij2, intN + intDlOtr, ij1, fill='black', width=5)
            time.sleep(fltTimeDelay)
            canvas.update()
            ij2 = ij1
            intN += intDlOtr

        intN = 0
        ii = intCanvasSize // 3 * 2
        ij2 = ii
        while intN < intCanvasSize:
            ij1 = rnd.randint(ii - 4, ii + 4)
            canvas.create_line(intN, ij2, intN + intDlOtr, ij1, fill='black', width=5)
            time.sleep(fltTimeDelay)
            canvas.update()
            ij2 = ij1
            intN += intDlOtr
    else:
        canvas.create_line(intCanvasSize // 3, 0, intCanvasSize // 3, intCanvasSize, fill='black', width=5)
        canvas.create_line(intCanvasSize // 3 * 2, 0, intCanvasSize // 3 * 2, intCanvasSize, fill='black', width=5)
        canvas.create_line(0, intCanvasSize // 3, intCanvasSize, intCanvasSize // 3, fill='black', width=5)
        canvas.create_line(0, intCanvasSize // 3 * 2, intCanvasSize, intCanvasSize // 3 * 2, fill='black', width=5)


def init_koor():
    global tplKoorKvN
    global tplKoorKvK
    global intCanvasSize

    tplKoorKvN = ((0, 0), (intCanvasSize // 3, 0), (intCanvasSize // 3 * 2, 0),
                  (0, intCanvasSize // 3), (intCanvasSize // 3, intCanvasSize // 3),
                  (intCanvasSize // 3 * 2, intCanvasSize // 3),
                  (0, intCanvasSize // 3 * 2), (intCanvasSize // 3, intCanvasSize // 3 * 2),
                  (intCanvasSize // 3 * 2, intCanvasSize // 3 * 2))

    tplKoorKvK = ((intCanvasSize // 3, intCanvasSize // 3), (intCanvasSize // 3 * 2, intCanvasSize // 3),
                  (intCanvasSize, intCanvasSize // 3),
                  (intCanvasSize // 3, intCanvasSize // 3 * 2), (intCanvasSize // 3 * 2, intCanvasSize // 3 * 2),
                  (intCanvasSize, intCanvasSize // 3 * 2),
                  (intCanvasSize // 3, intCanvasSize), (intCanvasSize // 3 * 2, intCanvasSize),
                  (intCanvasSize, intCanvasSize))


def init_data():
    global lstDate
    global blnPaintZero
    global blnWin
    global blnEEE

    lstDate = [[0 for _ in range(3)] for _ in range(3)]
    blnPaintZero = False
    blnWin = False
    blnEEE = False


def button2_click():
    global blnStyleLine

    blnStyleLine = not blnStyleLine


def button1_click():
    global canvas

    canvas.delete('all')
    init_data()
    paint_cells()


rnd.seed()
# Задержка при рисовании линии
fltTimeDelay = 0.05
# Длина отрезка при рисовании линии для создания кривой
intDlOtr = 20
# Шаг радиана для рисования окружности
fltStepRad = 0.5
# Ширина окна
intScrSize1 = 600
# Высота окна
intScrSize2 = 700
# Размер канвы
intCanvasSize = 600
# Тип рисунка - прямые или кривые линии
blnStyleLine = True

blnWin = False
blnEEE = False
lstDate = []

pScr = tk.Tk()
pScr.title('Крестики - Нолики!!!')
pScr.minsize(intScrSize1, intScrSize2)
pScr.maxsize(intScrSize1, intScrSize2)
pScr.resizable(False, False)
canvas = tk.Canvas(pScr, width=intCanvasSize, height=intCanvasSize)
canvas.pack()

init_data()
init_koor()
paint_cells()

canvas.bind('<Button-1>', click_left)

button1 = tk.Button(pScr, text='Начать игру заново', command=button1_click)
button1.pack(side='left')

button2 = tk.Button(pScr, text='Сменить тип линий', command=button2_click)
button2.pack(side='left')

pScr.mainloop()

