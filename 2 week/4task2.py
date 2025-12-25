n, m = map(int, input().split())
lecture_text = input().strip()

distinct_words = set()

for i in range(n - m + 1):
    word = lecture_text[i:i+m]
    distinct_words.add(word)

print(len(distinct_words))
