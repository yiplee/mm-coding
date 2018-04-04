def maxnum(nums):
    if len(nums)==1:
        return nums[0]
    else:
        return nums[0] if nums[0]>maxnum(nums[1:]) else maxnum(nums[1:])
print maxnum([4,2,6,1,0])
