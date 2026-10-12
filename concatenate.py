# program to concatenate two singly linked lists in python

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def insert(self, data):
        new_node = Node(data)

        if self.head is None:
            self.head = new_node
        else:
            temp = self.head
            while temp.next:
                temp = temp.next
            temp.next = new_node

    def concatenate(self, list2):
        if self.head is None:
            self.head = list2.head
            return

        temp = self.head
        while temp.next:
            temp = temp.next

        temp.next = list2.head

    def display(self):
        temp = self.head
        while temp:
            print(temp.data, end=" -> ")
            temp = temp.next
        print("None")


# Create first linked list
list1 = LinkedList()
list1.insert(10)
list1.insert(20)
list1.insert(30)

# Create second linked list
list2 = LinkedList()
list2.insert(40)
list2.insert(50)
list2.insert(60)

print("First linked list:")
list1.display()

print("Second linked list:")
list2.display()

# Concatenate the lists
list1.concatenate(list2)

print("Concatenated linked list:")
list1.display()

