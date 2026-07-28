def moveZeroes(nums):
    insert_pos = 0
    
   
    for i in range(len(nums)):
        if nums[i] != 0:
            nums[insert_pos] = nums[i]
            insert_pos += 1
    
    
    for i in range(insert_pos, len(nums)):
        nums[i] = 0
    
    return nums


print(moveZeroes([0,5,0,3,12]))  
print(moveZeroes([0]))          