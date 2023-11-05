#resavanje "simetrijom"
from math import sqrt

def kategorizacija(lista):
    lista.sort()
    k = []
    for i in range(len(lista)):
        e = lista[i]
        if i > 0:
            if k[-1][0] == e:
                k[-1][1] = k[-1][1] + 1
            else:
                k.append([e, 1])
        else:
            k.append([e, 1])
    return k

#funkcija je ustvari nepotrebna, svi cinioci ce ionako biti prosti
def prost(x):
    for i in range(1, int(x ** 0.5) + 1):
        if (x % i) == 0 and i > 1:
            return False
    return True
           
p = int(input())

nzd = 1

faktorizacija = []

while p != 1:
    for i in range(2, p + 1):
        if p % i == 0:
            if prost(i):
                faktorizacija.append(i)
                p //= i
                break
#nice
for e in kategorizacija(faktorizacija):
    if e[1] > 1:
        nzd *= e[0] ** int(e[1] / 2)

print(nzd)
