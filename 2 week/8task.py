def is_anagram(s1, s2):
    if sorted(s1) == sorted(s2):
        return "YES"
    else:
        return "NO"

s1 = input()
s2 = input()

print(is_anagram(s1, s2))
