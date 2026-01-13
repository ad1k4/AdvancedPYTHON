import string

def analyze_text(input_file, output_file):
    lines_count = 0
    words_count = 0
    word_frequency = {}

    try:
        # [cite_start]Use context manager with [cite: 17]
        with open(input_file, 'r', encoding='utf-8') as f:
            for line in f:
                lines_count += 1
                
                # [cite_start]Ignore punctuation and case sensitivity [cite: 18]
                clean_line = line.translate(str.maketrans('', '', string.punctuation)).lower()
                words = clean_line.split()
                
                words_count += len(words)
                
                for word in words:
                    if word in word_frequency:
                        word_frequency[word] += 1
                    else:
                        word_frequency[word] = 1

        # [cite_start]Save the analysis result into analysis.txt [cite: 15]
        with open(output_file, 'w', encoding='utf-8') as f:
            f.write(f"Total number of lines: {lines_count}\n")
            f.write(f"Total number of words: {words_count}\n")
            f.write("Word frequency:\n")
            for word, count in word_frequency.items():
                f.write(f"{word}: {count}\n")
        
        print("Analysis saved to analysis.txt")

    except FileNotFoundError:
        print(f"File {input_file} not found.")

if __name__ == "__main__":
    # Create dummy file for testing
    with open("text.txt", "w") as f:
        f.write("Hello world! Hello Python.\nThis is a test file.")
        
    analyze_text("text.txt", "analysis.txt")