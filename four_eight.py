def multiply_table(nums):
    
    for i in range(2,10):
        for j in nums:
            j=j*i
        return nums
print multiply_table([2,3,7,8,10])