# programm logics 

# for finding middle node and deleting it

def findmid_del(self):
    temp = temp1 = self.head
    prev=None
    while temp1 and temp1.next:
        prev = temp
        temp = temp.next
        temp1=temp1.next.next
    print("Middle node: ",temp.data)
    prev.next = temp.next
    temp = None 

 # for deleting first and last node 

def delfirst_last(self):
    temp1 = self.head
    temp1 = None
    prev = None
    temp = self.head = self.head.next 
    while(temp.next):
        prev = temp
        temp = temp.next
    prev.next=None
    temp = None

# delete alternate nodes in singly linked list

def del_alternate(self):
    prev = self.head
    temp = self.head.next

    while prev and temp:
        prev.next = temp.next
        temp = None # actual deletion of node
        prev = prev.next 

        if prev:
            temp = prev.next

