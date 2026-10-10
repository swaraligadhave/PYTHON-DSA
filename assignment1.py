#creating a singly linked list
class Node:
    def __init__(self,data):
        self.data = data
        self.next = None
#1. create linked list
class LinkedList:
    def __init__(self):
        self.head = None

    def append(self,data):
        new_node = Node(data)

        if self.head is None:
            self.head = new_node
        else:
            temp = self.head
            while temp.next:
                temp = temp.next
            temp.next = new_node

    #2. traverse and print
    def print(self):
        temp = self.head
        while temp:
            print(temp.data, end=" -> ")
            temp = temp.next
        print("None")

    # 3.insert at a specific position
    def insert(self,data,pos):
        new_node = Node(data)

        if pos < 1:
            print("Invalid Position")
            return

        if pos == 1:
            new_node.next = self.head 
            self.head = new_node
            return
        
        temp = self.head
        for i in range(pos-2):
            if temp is None:
                print("Invalid position")
                return
            temp = temp.next

        if temp is None:
            print("Invalid position")
            return
        
        new_node.next = temp.next
        temp.next = new_node

    #4. Find middle node

    def middle(self):
        slow = self.head
        fast = self.head

        if self.head is None:
            print("List is empty")
            return

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        print("Middle node:",slow.data)


    # 5.delete node by value
    def delete(self,key):
        temp = self.head
    
        if temp and temp.data == key:
            self.head = temp.next
            return
    
        while temp and temp.next:
            if temp.next.data == key:
                temp.next = temp.next.next 
                return
            temp = temp.next

    # 6.reverse linked list
    def reverse(self):
        prev = None
        curr = self.head

        while curr:
            next_node = curr.next
            curr.next = prev
            prev = curr
            curr = next_node

        self.head = prev

    # 7.sum of every two consecutive nodes
    def sum(self):
        temp = self.head

        while temp and temp.next:
            print(temp.data + temp.next.data)
            temp = temp.next
            
#main 
list = LinkedList()

#create 
list.append(10)
list.append(20) 
list.append(30)
list.append(40)
list.append(50)      

print("Singly Linked List created")
list.print()

#insert a node at a specific position
list.insert(24,2)
print("After insertion:")
list.print()

#middle node
list.middle()

#delete
list.delete(40)
print("After deletion:")
list.print()

#reverse
list.reverse()
print("After reversing:")
list.print()

#sum of two consecutive nodes
print("Sum of every two consecutive nodes:")
list.sum()