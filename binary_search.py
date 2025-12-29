
def binary_search(nums,left,right,t):
    if left>right:
        return -1
    m = (left+right)//2
    if t==nums[m]:
        return m
    elif t<nums[m]:
        return binary_search(nums, left, m-1,t)
    else:
        return binary_search(nums, m+1, right, t)
    
    '''while left<=right:
        m=(left+right)//2
        if nums[m]==t:
            return m
        elif nums[m]<t:
            left = m+1
        else:
            right = m-1
    return -1
    '''    
print("if you can explain it in one sentence then its a good commit")
nums = [10,20,30,40,50,60,70]
n = len(nums)
t=62
pos = binary_search(nums, 0, n, t)
print(pos)