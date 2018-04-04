#coding=utf-8
# def quicksort(nums):
#     less=[]
#     right=[]
#     if len(nums)<2:
#         return nums
#     else:
#         temp=nums[0]
#         for i in nums[1:]:
#             if i<temp:
#                 less.append(i)
#         for i in nums[1:]:
#             if i >temp:
#                 right.append(i)
#         return  quicksort(less)+[temp]+quicksort(right)
# print quicksort([5,3,9,0,6])


#coding=utf-8
#更简便的写法
def quicksort(nums):
    if len(nums)<2:
        return nums
    else:
        temp=nums[0]
        less=[i for i in nums[1:] if i<=temp]
        right=[i for i in nums[1:] if i>temp]
        return quicksort(less)+[temp]+quicksort(right)
print quicksort([5,3,9,0,6])