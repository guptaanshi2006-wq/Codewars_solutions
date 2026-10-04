def find_average(nums):
    #your code here
    num=len(nums)
    sum=0
    for i in nums:
        sum=sum+i
    avg=sum/num
    return avg