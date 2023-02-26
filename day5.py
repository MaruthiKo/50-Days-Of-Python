def my_discount():
    n = int(input())
    m = int(input())
    b = float(m/100)*n
    a = n - b
    return a

print(my_discount())