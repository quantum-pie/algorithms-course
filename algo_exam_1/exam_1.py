a, b = map(int, input().split())
m, n = a, b
while m != 0 and n != 0:
    if m > n:
        m = m % n
    else:
        n = n % m

print((a * b) // (m + n))