#coding=utf-8
#使用两种方法编写：递归和循环
#递归
def sum(nums):
    if nums==[]:
        return 0
    else:
        return nums[0]+sum(nums[1:])
print sum([1,2,3,4])