import re

def check_license_plate(plate):
    pattern = r'^[A, B, C, E, H, K, M, O, P, T, X, Y]{1}\d{3}[A, B, C, E, H, K, M, O, P, T, X, Y]{2}$'
    if re.match(pattern, plate):
        return "Yes"
    else:
        return "No"

n = int(input())

for _ in range(n):
    plate = input().strip()
    print(check_license_plate(plate))
