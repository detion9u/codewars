def removeElement(nums, val):
    # idx = nums.index(val)
    len1 = len(nums)
    # for i in range(len1):
    #     if nums[i] == val:
    #         idx = i
    #         while(idx + 1 < len1):
    #             if nums[idx + 1] != val:
    #                 nums[i] = nums[idx + 1]
    #                 break    
            
    #             idx = idx + 1    
    #         else:
    #             nums[idx] = '#'    
    for i in range(len1):
        if nums[i] == val:
            nums[i] = '#'


            
    while(nums.count('#') > 0):
        nums.remove('#')

    len1 = len(nums)    
    return len1
    print(nums)
    # return(nums)
    

    return 
if __name__ == '__main__':
    print("Hello Python!")   
    removeElement([3,2,2,3],3)