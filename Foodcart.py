class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.breakpoint = None
        self.newLink = None


class LinkedList:
    def __init__(self):
        self.head = None

    def isElement(self):
        if self.head is None:
            return False
        else:
            return True
        
    def insBeg(self, data):
        new = Node(data)
        new.next = self.head
        self.head = new
  
    
    def display(self):
        temp = self.head
        while temp is not None:
            print(temp.data, end=" - > ")
            temp = temp.next
        print(None)

    def solution(self):
        kart2 = self.head
        #counting elemets
        count = 0
        while kart2 is not None:
            # print(temp.data, end=" - > ")
            count += 1
            kart2 = kart2.next
        # print(count)


        #Dividing
        stop = count / 2
        count = 0
        kart2 = self.head
        # print(count, stop)
        while kart2 is not None:
            if count == stop:
                self.breakpoint = kart2.data
                # print("Break point: ",kart2.data)
                return
            count += 1
            kart2 = kart2.next

    def making(self):
        temp = self.head

        while temp is not None:
            if(temp.next.data == self.breakpoint):
                self.newLink = temp.next
                temp.next = None
            temp = temp.next

        print("New Queue: ")    
        temp = self.newLink
        while temp is not None:
            print(temp.data, end=" - > ")
            temp = temp.next
        print(None)
                



l = LinkedList()
l.insBeg(10)
l.insBeg(20)
l.insBeg(30)
l.insBeg(40)
l.insBeg(50)
l.insBeg(60)

l.insBeg(210)
l.insBeg(20)
l.insBeg(30)
l.insBeg(40)
l.insBeg(50)
l.insBeg(60)

print("Whole List : ")
l.display()

l.solution()
l.making()
print("Old Queue: ")
l.display()