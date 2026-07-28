nums=[1,2,3,1]
def duplicate(nums):
    return len(nums) != len(set(nums))
print("Output:",duplicate(nums))

