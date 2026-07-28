nums=[1,2,3,4]
def duplicate(nums):
    return len(nums) != len(set(nums))
print("Output:",duplicate(nums))

