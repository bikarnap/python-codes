def mysplit(strng):
    lst = []
    word = ''
    for ch in strng:
        if ch != ' ':
            word += ch
        if ch == ' ':
            if len(word) > 0:
                lst.append(word)
            word = ''
    if word:
        lst.append(word)
    if len(lst) == 0:
        return []
    return lst
print(mysplit("To be or not to be, that is the question"))
print(mysplit("To be or not to be,that is the question"))
print(mysplit("   "))
print(mysplit(" abc "))
print(mysplit(""))