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

    def insert_beginning(self, data):
        newnode = Node(data)

        newnode.next = self.head
        self.head = newnode

    def traverse(self):
        current = self.head

        while current is not None:
            print(current.data, end=" -> ")
            current = current.next

        print("None")


ll = LinkedList()

ll.add(10)
ll.add(20)
ll.add(30)

print("Before insertion:")
ll.traverse()

ll.insert_beginning(5)

print("After insertion:")
ll.traverse()