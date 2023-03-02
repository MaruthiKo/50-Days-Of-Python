def odd_even(nums):
    even_list = []
    odd_list = []
    for num in nums:
        if(num % 2 == 0):
            even_list.append(num)
        else:
            odd_list.append(num)
    
    even_list = sorted(even_list)
    odd_list = sorted(odd_list)
    return even_list[-1] - odd_list[0]

print(odd_even([1,2,4,6]))

