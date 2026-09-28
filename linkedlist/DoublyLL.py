class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None


class DoublyCircularLinkedList:
    def __init__(self):
        self.head = None

    def isElement(self):
        if self.head is None:
            return False
        else:
            return True

    def insBeg(self, data):
        new = Node(data)

        if self.head is None:
            new.next = new
            new.prev = new
            self.head = new
            return

        last = self.head.prev        # O(1) thanks to prev pointer

        new.next = self.head
        new.prev = last

        last.next = new
        self.head.prev = new

        self.head = new

    def insEnd(self, data):
        new = Node(data)

        if self.head is None:
            new.next = new
            new.prev = new
            self.head = new
            return

        last = self.head.prev

        new.next = self.head
        new.prev = last

        last.next = new
        self.head.prev = new

    def atSpecific(self, data, key):
        if self.isElement():
            new = Node(data)
            temp = self.head

            while True:
                if temp.data == key:
                    nxt = temp.next

                    new.next = nxt
                    new.prev = temp

                    temp.next = new
                    nxt.prev = new
                    return True

                temp = temp.next
                if temp == self.head:      # went all the way around
                    break
            return False
        return False

    def delAtFront(self):
        if self.isElement():
            if self.head.next == self.head:    # only one node
                self.head = None
                return True

            last = self.head.prev
            new_head = self.head.next

            last.next = new_head
            new_head.prev = last
            self.head = new_head
            return True
        return False

    def delAtEnd(self):
        if self.isElement():
            if self.head.next == self.head:    # only one node
                self.head = None
                return True

            last = self.head.prev
            new_last = last.prev

            new_last.next = self.head
            self.head.prev = new_last
            return True
        return False

    def delSpecific(self, key):
        if self.isElement():
            if self.head.data == key:
                return self.delAtFront()

            temp = self.head.next
            while temp != self.head:
                if temp.data == key:
                    temp.prev.next = temp.next
                    temp.next.prev = temp.prev
                    return True
                temp = temp.next
            return False
        return False

    def display(self):
        if self.head is None:
            print(None)
            return

        temp = self.head
        while True:
            print(temp.data, end=" <-> ")
            temp = temp.next
            if temp == self.head:
                break
        print("(back to head)")


l = DoublyCircularLinkedList()

l.insBeg(10)
l.insBeg(20)
l.insBeg(30)
l.insBeg(40)
l.insEnd(45)
l.insEnd(98)
l.insEnd(300)
l.insEnd(450)

print("Original Linked list: ")
l.display()

# Adding Element at specific position
# key = int(input('Enter key: '))
# l.atSpecific(69, key)

l.delAtFront()
print("Delete First Element: ")
l.display()

l.delAtEnd()
print("Delete Last Element: ")
l.display()

l.delSpecific(98)
print("Delete element 98 :")
l.display()