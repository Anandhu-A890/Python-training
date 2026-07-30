print("Who is the imposter?")
n=int(input("Enter crew number:"))
x=1
while x*2<=n:
    x*=2

survivor=1+(n-x)*2

print(survivor)
        