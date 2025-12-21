a = input().strip()
b = input().strip()
m = len(b)
bb = b + b
shifts = []
for k in range(m):
    shifts.append(bb[k:k+m])
count = 0
for i in range(len(a) - m + 1):
    sub = a[i:i+m]
    if sub in shifts:
        count += 1
print(count)