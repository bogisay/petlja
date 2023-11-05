brojevi = []
for i in range(4):
    brojevi.append(int(input()))

#Moguce je resiti i slice-ovanjem
def exclude(lista, index):
    r = []
    for i in range(len(lista)):
        if i != index:
            r.append(lista[i])

    return r

def najmanja(lista, i):
    r = "f"
    for c in lista:
        if r == "f":
            r = abs(c - i)
        elif abs(c - i) < r:
            r = abs(c - i)
    return r

najdalji = [[brojevi[0], najmanja(exclude(brojevi, 0), brojevi[0])]]

for i in range(1, len(brojevi)):
    m = najmanja(exclude(brojevi, i), brojevi[i])
    
    if najdalji[0][1] > m:
        continue

    elif najdalji[0][1] == m:
        najdalji.append([brojevi[i], m])
    
    elif najdalji[0][1] < m: 
        najdalji = [[brojevi[i], m]]

r = []

for i in najdalji:
    r.append(i[0])
r.sort()
for i in r:
    print(i)
