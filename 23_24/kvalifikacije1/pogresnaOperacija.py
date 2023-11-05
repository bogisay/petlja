#def nzd(a, b):
#    if b == 0:
#        return a
#    return (b, a % b)


n = int(input())

#d = nzd(n,n-1)

#x = n / d
#y = (n-1) / d

# Skracivanje je ipak nepotrebno, jer gcd(n, n - 1)

x = n
y = n-1

print(f"{x}/{y}")

