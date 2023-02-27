def get_username(mail):
    s = ""
    char = 0
    while mail[char] != '@':
        s += mail[char]
        char += 1
    return s

print(get_username('ben@gmail.com'))