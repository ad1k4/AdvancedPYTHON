n = int(input())

res = []
for x in range(1, n + 1):
    s = str(x)
    ok = True
    for ch in s:
        d = int(ch)
        if d == 0 or x % d != 0:
            ok = False
            break
    if ok:
        res.append(x)

print(*res)
