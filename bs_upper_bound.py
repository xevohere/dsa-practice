def lower_bound(nums, low, high, target):
    ans = high-low+1
    
    while low<=high:
        mid=(low+high)//2
        
        if nums[mid]>target:
            ans=mid
            high = mid-1
            
        else:
            low = mid+1
    return ans 

nums=[101,102,103,104,104,104,104,110, 115,119]
p=lower_bound(nums, 0, 9, 104)
print(p)