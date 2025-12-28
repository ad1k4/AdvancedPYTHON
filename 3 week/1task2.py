def calculate_sum_and_mean(arr):
    arr_sum = sum(arr)
    arr_mean = arr_sum / len(arr) if arr else 0
    return arr_sum, arr_mean

array1 = [1, 2, 3, 4, 5]
array2 = [10, 20, 30, 40, 50]
array3 = [7, 14, 21, 28, 35]

sum1, mean1 = calculate_sum_and_mean(array1)
sum2, mean2 = calculate_sum_and_mean(array2)
sum3, mean3 = calculate_sum_and_mean(array3)

print(f"Array 1: Sum = {sum1}, Mean = {mean1:.2f}")
print(f"Array 2: Sum = {sum2}, Mean = {mean2:.2f}")
print(f"Array 3: Sum = {sum3}, Mean = {mean3:.2f}")





