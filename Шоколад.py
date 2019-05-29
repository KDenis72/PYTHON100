def inputnum(strStr):
    blnKl = True
    n = 0
    while blnKl:
        print('Введите число ' + strStr + ':', end=' ')
        n = input()
        if n.isdigit():
            n = int(n)
            if n > 0:
                blnKl = False
    return n


n = inputnum('n')
m = inputnum('m')
k = inputnum('k')

if (k % n == 0 or k % m == 0) and n * m > k:
    print('YES')
else:
    print('NO')



