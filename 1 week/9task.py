a=int(input())
i=a//1000
s=a%1000
first_sum= i//100 + (i//10)%10 + i%10
second_sum = (s // 100) + ((s // 10) % 10) + (s % 10)
if first_sum == second_sum:
    print("YES")
else:
    print("NO")

