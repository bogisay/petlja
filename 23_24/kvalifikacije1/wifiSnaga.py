m = int(input())
kuce = list(map(int, input().split()))
n = int(input())
predajnici = list(map(int, input().split()))

d = 0

for kuca in kuce:
    najmanja = abs(predajnici[0] - kuca)
    for predajnik in predajnici[1:]:
        if abs(kuca - predajnik) < najmanja:
            najmanja = abs(kuca - predajnik)
    if d < najmanja:
        d = najmanja

print(d)

