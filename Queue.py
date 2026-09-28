class Queue:
    def __init__(self):
        self.queue = []

    # Enqueue
    def enqueue(self, data):
        self.queue.append(data)

    # Dequeue
    def dequeue(self):
        if len(self.queue) == 0:
            print("Queue Underflow")
            return None

        return self.queue.pop(0)

    # Peek
    def peek(self):
        if len(self.queue) == 0:
            print("Queue is empty")
            return

        print("Front element:", self.queue[0])

    # Display
    def display(self):
        if len(self.queue) == 0:
            print("Queue is empty")
            return

        print("Queue:")

        for i in range(len(self.queue)):
            print(self.queue[i], end=" -> ")

        print("None")

    # Check empty
    def isEmpty(self):
        return len(self.queue) == 0


q = Queue()


while True:

    print("\n----- QUEUE MENU -----")
    print("1. Enqueue")
    print("2. Dequeue")
    print("3. Peek")
    print("4. Display")
    print("5. Check if Empty")
    print("6. Exit")

    choice = int(input("Enter your choice: "))

    if choice == 1:

        data = int(input("Enter data: "))
        q.enqueue(data)
        print("Element enqueued successfully.")

    elif choice == 2:

        element = q.dequeue()

        if element is not None:
            print("Dequeued element:", element)

    elif choice == 3:

        q.peek()

    elif choice == 4:

        q.display()

    elif choice == 5:

        if q.isEmpty():
            print("Queue is empty")
        else:
            print("Queue is not empty")

    elif choice == 6:

        print("Program terminated.")
        break

    else:

        print("Invalid choice. Please try again.")