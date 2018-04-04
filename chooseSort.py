#coding=utf-8
'''把数组元素按照从小到大排序
   先定义一个选出最小数的函数
   然后排序'''
def choose_min(nums):
    if nums==None:
        return
    min=nums[0]
    for i in range(0,len(nums)):
        if nums[i]<=min:
            min=nums[i]
        i+=1
    return min                        
#调用上面函数进行排序
def sort(nums):
    new_nums=[]
    while len(nums)>1:
        current=choose_min(nums)
        new_nums.append(current)
        nums.remove(current)
    new_nums.append(nums[-1])
    return new_nums

print sort([4,7,9,2,0,1])
    
