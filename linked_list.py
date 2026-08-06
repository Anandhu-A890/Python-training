class Linknode:
    def __init__(self,val,next=None):
        self.val=val
        self.next=next
head=Linknode(5)
a,b,c,d=(Linknode(1),Linknode(3),Linknode(4),Linknode(7))
head.next=a
a.next=b
b.next=c
c.next=d
# print(c.val)
# print(c.next.val)
current=head
# while current is not None:
#     print(current.val,end="->")
#     current=current.next
#     if current is None:
#         print("None")

target=int(input("Enter a number to check in linked list:")) #item is in linked list
while current:
    if target==current.val:
        found=True
        break
    current=current.next

if found:
    print("It is present in the linked list")
else:
    print("It is not present in the linked list")
