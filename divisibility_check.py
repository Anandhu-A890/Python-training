number=int(input("Enter a number:"))
if (number%3==0)and(number%5==0):
    print("Kizzbuzz")
elif number%5==0:
    print("Buzz")
elif number%3==0:
    print("Fizz")
else:
    print(f"The entered numbered is :{number}")