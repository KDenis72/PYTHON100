import time
import matplotlib as mpl
import matplotlib.pyplot as plt


def my_fab(count_for):
    def deccc(ff):
        def new_ff(*ar, **kv):
            end_time = 0
            for _ in range(count_for):
                st_time = time.time()
                par = ff(*ar, **kv)
                end_time += time.time() - st_time

            print(end_time / count_for)

            return par

        return new_ff
    return deccc


@my_fab(10)
def cc_sim(sss):
    return {i: sss.count(i) for i in set(sss)}


@my_fab(10)
def cc_sim1(sss):
    d = {}
    for i in set(sss):
        d[i] = sss.count(i)

    return d


@my_fab(10)
def cc_sim2(sss):
    d = {}
    for i in sss:
        if i in d:
            d[i] += 1
        else:
            d[i] = 1

    return d


ss = open('./data.txt', mode='r', encoding='utf-8').read()
# ss = ff.read()
# ff.close()
ss = ss.replace(' ', '')
ss = ss.lower()

ssl = cc_sim(ss)
ssl1 = cc_sim1(ss)
ssll = cc_sim2(ss)


print('Всего символов - ' + str(len(ss)))
print('Всего уникальных символов  - ' + str(len(ssl)))

lstSim = sorted(ssl, key=lambda x: ssl[x], reverse=True)[:10]
lstCount = [ssl[i] for i in lstSim]
print(lstSim)
print(lstCount)

mpl.rcParams.update({'font.size': 10})
plt.title('10 самых встречающихся символов!!!')
plt.xlabel('Буквы')
plt.ylabel('Количество, шт.')
plt.bar(lstSim, lstCount, color='blue')

plt.show()

