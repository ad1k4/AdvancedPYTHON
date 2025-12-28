def sort_string(input_string):
    words = input_string.split()
    sorted_words = [''.join(sorted(word)) for word in words] 
    return ' '.join(sorted_words)

input_string = "hello world"
sorted_string = sort_string(input_string)
print("Sorted string:", sorted_string)
