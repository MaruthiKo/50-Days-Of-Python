def isPrime(num):
    for i in range(2,num):
        if num % i == 0:
            return False
    return True

def prime_numbers():
    n = int(input("Enter a number:"))
    nums = []
    for num in range(2,n):
        if(isPrime(num)):
            nums.append(num)
    return nums

print(prime_numbers())