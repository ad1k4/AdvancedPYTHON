def all_eq(lst):
    max_length = max(len(s) for s in lst)
    return [s.ljust(max_length, '_') for s in lst]
strings = ["cat", "elephant", "dog"]
result = all_eq(strings)
print(result)