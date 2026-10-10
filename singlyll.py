# singly linear linked list
class Node:
    def __init__(self,val):
        self.data = val
        self.next = None 

class LinkedList:
    def __init__(self):
        self.head=None
    def append(self,new_node):
        if(self.head==None):
            self.head=new_node
        else:
            temp = self.head
            while(temp.next): #this means temp.next is not null 
                temp = temp.next  # traverse list until the value is null,if not go to the next node
            temp.next=new_node # append new node

    def insert(self,new_node,pos):
        temp = self.head
        if pos == 1: # inserting at first position
            new_node.next = self.head
            self.head = new_node

        else:
            p = 1
            while(p!=pos-1): #or #temp.next!=None(for inserting at any position)):
                temp = temp.next
                p += 1
            new_node.next = temp.next
            temp.next = new_node
    
    def del_node(self,value): #deleting first node 
        temp = self.head 
        prev = None
        if temp.data == value: 
            self.head = self.head.next
            return

        while(temp):
            if temp.data == value:
                break
            else:
                prev = temp
                temp = temp.next
        if temp == None:
            print("Value is not there in list")

        prev.next = temp.next
        temp = None

        def reverse(self): #reversing the list
            curr = self.head
            prev = None
            while(curr):
                nextnode=curr.next
                curr.next=prev
                prev = curr
                curr = nextnode
            self.head = prev
            

    def print(self):
        # sum = 0 #sum of even/odd values
        temp = self.head
        # while temp: #checks if temp has some data 
        #     if temp.data>0:
        #         sum+= temp.data
        #     temp=temp.next
        # print(sum)
        while temp.next:
            print(temp.data)
            temp=temp.next
        if temp:
            print(temp.data)


list=LinkedList()
n1=Node(10)
n2=Node(20)
n3=Node(30)
n4=Node(50)
list.append(n1)
list.append(n2)
list.append(n3)
list.append(n4)
list.append(Node(40))
list.insert(Node(100),1)
list.print()
list.insert(Node(66),4)
list.print()
list.insert(Node(80),7)
list.print()
list.insert(Node(90),8)
list.print()
list.del_node(45) # gives output as value not there in list 
list.print()
