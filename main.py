a = -11 * 7 * 5 * 8
def sushu(a):
    r = []
    a = int(a)
    if a < 0:
        r.append(-1)
        a = abs(a)
    while a != 1:
        i = 2
        while i <= a:
            if a % i == 0:
                r.append(i)
                a = int(a / i)
                break
            i = i + 1
    return r
print(sushu(a))
