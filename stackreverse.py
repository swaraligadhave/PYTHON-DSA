class Node:
    def __init__(self, value):
        self.data = value
        self.next = None

class stack:
    def __init__(self):
        self.top = None

    def isEmpty(self):
        return self.top is None

    def push(self, new_node):
        new_node.next = self.top
        self.top = new_node

    def pop(self):
        if self.isEmpty():
            print("Stack is empty")
        else:
            temp = self.top
            print("Popped element:", temp.data)
            self.top = self.top.next
            temp = None

    def reverse(self):
        temp = self.top
        while temp:
            st1.push(Node(temp.data))
            temp = temp.next
     
    
    def print(self):
        if self.isEmpty():
            print("Stack is empty")

        else:
            print("Stack contains:")
            temp = self.top
            while temp:
                print(temp.data)
                temp = temp.next 

st = stack()
st1 = stack()
st.push(Node(10))
st.push(Node(20))
st.push(Node(30))
st.push(Node(40))
st.push(Node(50))
st.print()
st.pop()
st.print()
st.reverse()
st1.print()