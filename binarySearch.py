def binarysearch(nums,x):
    if nums==None:
        return None
    low=0
    high=len(nums)-1
    while low<=high:
        mid=(low+high)/2
        guess=nums[mid]
        if guess==x:
            return mid
        elif guess<x:
            low=mid+1
        elif guess>x:
            high=mid-1
    return None
    