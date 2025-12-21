text = input().strip()
count = 0
for i in range(len(text) - 4):
    part = text[i:i+5]
    if part == ">>-->":
        count += 1
    if part == "<--<<":
        count += 1
print(count)