n = int(input())
k = int(input())
z1 = 0

for i in range(k):
    z1 += int(input())

p = float(input())

# p = (z1 + z2) / n
#nesto predosecam da ce ovde biti nekog problema
z2 = round(p * n, 0) - z1

p1 = float(z2) / (n - k)

print(format(p1, '.2f'))

