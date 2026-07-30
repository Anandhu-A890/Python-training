a=input("Enter a word:")
if(a[0::]==a[::-1]):
    print("Yes, it is")
else:
    print("No, it is not a palindrome")