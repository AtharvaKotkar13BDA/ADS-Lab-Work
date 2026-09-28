class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def add(self, data):
        newnode = Node(data)

        if self.head is None:
            self.head = newnode
        else:
            current = self.head
            while current.next is not None:
                current = current.next
            current.next = newnode


# Creating linked list
ll = LinkedList()

# Adding nodes
ll.add(10)
ll.add(20)
ll.add(30)
ll.add(40)

print("Nodes created successfully.")