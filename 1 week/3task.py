a = float(input())
integer_part = int(a)
second_part = int((a*100)%100)
new_i=integer_part / 100
new_s=second_part * 100
print(new_i + new_s)