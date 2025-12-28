def swap_first_last(arr):
    if len(arr) > 1:
        arr[0], arr[-1] = arr[-1], arr[0]

m = int(input())
a = list(map(int, input().split()))

original = a[:]
swap_first_last(a)

print(*original)
print(*a)
