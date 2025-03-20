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

def sort_chars(charList):
    sortedList = []
    for char in charList:
        if char.isalpha() == False:
            continue
        entry = {
            "char": char,
            "num": charList[char]
        }
        sortedList.append(entry)
    sortedList.sort(reverse=True, key=sort_on)
    return sortedList

def sort_on(dict):
    return dict["num"]