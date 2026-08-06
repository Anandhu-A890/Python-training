print("------------------------------------------------------\n Hi! I am a Gennie. I can guess what number you think.\n Enter a range of values as input\n------------------------------------------------------")
   
def geenie(num,target):
    left,right=0,len(num)-1
    while left<=right:
        mid=left+(right-left)//2
        if num[mid]==target:
            return f"The number you guessed is at index {mid}"
        elif num[mid] < target:
            print(f"Check index{mid}-The number is towards right")
            left=mid+1
        else:
            print(f"Check index{mid}-The number is towards left")
            right=mid-1
    return f"Its not a number or its outside the range"
num=list(map(int,input("Enter a range of numbers:").split()))
target=int(input("Enter the number to be guessed:"))
guess=geenie(num,target)
print(guess)