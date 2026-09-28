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

    def insert(self, data, position):
        newnode = Node(data)

        if position == 0:
            newnode.next = self.head
            self.head = newnode
            return

        current = self.head
        prev_node = None
        count = 0

        while current is not None and count < position:
            prev_node = current
            current = current.next
            count += 1

        if count != position:
            print("Invalid position")
            return

        prev_node.next = newnode
        newnode.next = current

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
ll.add(40)

print("Before insertion:")
ll.traverse()

ll.insert(25, 2)

print("After insertion:")
ll.traverse()