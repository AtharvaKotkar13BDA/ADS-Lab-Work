class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    # Add node at end
    def add(self, data):
        newnode = Node(data)

        if self.head is None:
            self.head = newnode
            return

        current = self.head

        while current.next is not None:
            current = current.next

        current.next = newnode

    # Traverse
    def traverse(self):
        if self.head is None:
            print("List is empty")
            return

        current = self.head

        while current is not None:
            print(current.data, end=" -> ")
            current = current.next

        print("None")

    # Insert at beginning
    def insert_beginning(self, data):
        newnode = Node(data)

        newnode.next = self.head
        self.head = newnode

    # Insert at specific position
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

    # Delete from specific position
    def delete(self, position):

        if self.head is None:
            print("List is empty")
            return

        if position == 0:
            self.head = self.head.next
            return

        current = self.head
        prev_node = None
        count = 0

        while current is not None and count < position:
            prev_node = current
            current = current.next
            count += 1

        if current is None:
            print("Invalid position")
            return

        prev_node.next = current.next


# Create linked list
ll = LinkedList()


while True:

    print("\n----- LINKED LIST MENU -----")
    print("1. Add Node")
    print("2. Traverse")
    print("3. Insert at Beginning")
    print("4. Insert at Specific Position")
    print("5. Delete")
    print("6. Exit")

    choice = int(input("Enter your choice: "))

    if choice == 1:
        data = int(input("Enter data: "))
        ll.add(data)
        print("Node added successfully.")

    elif choice == 2:
        ll.traverse()

    elif choice == 3:
        data = int(input("Enter data: "))
        ll.insert_beginning(data)
        print("Node inserted at beginning.")

    elif choice == 4:
        data = int(input("Enter data: "))
        position = int(input("Enter position: "))
        ll.insert(data, position)
        print("Insertion completed.")

    elif choice == 5:
        position = int(input("Enter position to delete: "))
        ll.delete(position)
        print("Deletion completed.")

    elif choice == 6:
        print("Program terminated.")
        break

    else:
        print("Invalid choice. Please try again.")