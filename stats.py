def count_words(content):
    words = content.split()
    return len(words)

def count_chars(content):
    content = content.lower()
    charList = {}
    for char in content:
        if char in charList:
            charList[char] = charList[char] + 1
        else:
            charList[char] = 1
    return charList