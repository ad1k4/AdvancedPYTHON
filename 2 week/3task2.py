s = input().strip()

a = s[0]
op = s[1]
b = s[2]
c = s[4]

def to_int(ch):
    return int(ch)

if a == 'x':
    B = to_int(b)
    C = to_int(c)
    if op == '+':
        x = C - B
    else:  # '-'
        x = C + B

elif b == 'x':
    A = to_int(a)
    C = to_int(c)
    if op == '+':
        x = C - A
    else:  # '-'
        x = A - C

else:  # c == 'x'
    A = to_int(a)
    B = to_int(b)
    if op == '+':
        x = A + B
    else:  # '-'
        x = A - B

print(x)
