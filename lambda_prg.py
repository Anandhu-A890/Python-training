
# sq=lambda x:x*x
# print(sq(2))


# sq=list(map(lambda x:x*x,num))
# print(sq)

num=[i for i in range(1001)]
odd=list(filter(lambda x:x%2==1,num))
print(odd)