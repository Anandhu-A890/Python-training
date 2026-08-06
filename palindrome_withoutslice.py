n=input("Enter a string:")
def ispalindrome(n):
    length=len(n)
    for i in range(length//2):
        if n[i]!=n[length-1-i]:
            return False
    return True

if ispalindrome(n):
    print("It is palindrome")
else:
    print("Its not a palindrome")