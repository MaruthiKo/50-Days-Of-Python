def word_index(li):
    m = max(li)
    for i in range(len(li)):
        if all(len(li[i]) == len(li[0]) for li[i] in li):
            return 0
        elif m == li[i]:
            return i

print(word_index(['love','hate']))