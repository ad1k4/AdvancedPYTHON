from collections import Counter

def shopping_list_analysis(items):
    freq = Counter(items)
    print("Purchase frequency:")
    for item, count in freq.items():
        print(f"{item}: {count}")
    
    most_popular = max(freq, key=freq.get)
    print(f"\nMost popular item: {most_popular}")
    
    once_purchased = [item for item, count in freq.items() if count == 1]
    print(f"\nPurchased once: {' '.join(once_purchased)}")
    
    print("\nSorted by frequency:")
    for item, count in sorted(freq.items(), key=lambda x: x[1], reverse=True):
        print(f"{item} {count}")

items = input("Enter items purchased (space separated): ").split()
shopping_list_analysis(items)
