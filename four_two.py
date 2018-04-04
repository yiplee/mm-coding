def count(nums):
    if nums==[]:
        return 0
    else:
        return 1+count(nums[1:])
print count([1,2,3,4])