n = 1000
isBreak = False
for a in range(1, n):
    for b in range(1, n):
        c = (a ** 2 + b ** 2) ** 0.5
        if a + b + c == n and a < b < c:
            print(a, b, c)
            print(a * b * c)
            isBreak = True
            break
    if isBreak:
        break
