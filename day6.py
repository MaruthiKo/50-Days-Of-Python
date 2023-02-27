# def username(mail):
#     s = ""
#     i = 0
#     while mail[i]


# for i in l:
#     print(i,end=" ")

n = input("")
l = []
for i in range(len(n)):
    if n[i] == '@':
        break
    l.append(n[i])

for i in l:
    print(i, end="")