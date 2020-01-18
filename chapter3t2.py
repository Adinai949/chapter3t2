def sort():
    word = input('Введите слова через пробел: ')
    word = word.split()
    word.sort(key=len)
    word = ' '.join(word)
    return word
print(sort())