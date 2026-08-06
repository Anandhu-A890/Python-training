class doublyLinkNode:
    def __init__(self,val,next=None,prev=None):
        self.val=val
        self.next=next
        self.prev=prev
head=doublyLinkNode(1)
a,b,c,d=(doublyLinkNode(2),doublyLinkNode(3),doublyLinkNode(4),doublyLinkNode(7))
head.next=a
a.next=b
a.prev=head
b.next=c
b.prev=a
c.next=d
c.prev=b
current=head
while current is not None:
    print(current.val,end="<->")
    current=current.next
    if current is None:
        print("None")

    def insert_at_beginning(head,val):
        new_node=doublyLinkNode(val)
        new_node.next=head
        head.pev=new_node
        head=new_node
        return head
    Head=insert_at_beginning(Head,Tail,3)