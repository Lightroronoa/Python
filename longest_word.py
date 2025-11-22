def longest_word(s):
    words = s.split()
    if not words:
        return ""
    longest = words[0]
    for word in words:
        if len(word) > len(longest):
            longest = word
    return longest

# Example usage
sentence = input("Enter a sentence: ")
print(f"Longest word: {longest_word(sentence)}")