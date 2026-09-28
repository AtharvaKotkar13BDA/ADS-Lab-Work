class Stack:
    def __init__(self):
        self.stack = []

    # Push
    def push(self, data):
        self.stack.append(data)

    # Pop
    def pop(self):
        if len(self.stack) == 0:
            print("Stack Underflow")
            return

        return self.stack.pop()

    # Peek
    def peek(self):
        if len(self.stack) == 0:
            print("Stack is empty")
            return

        print("Top element:", self.stack[-1])

    # Display
    def display(self):
        if len(self.stack) == 0:
            print("Stack is empty")
            return

        print("Stack:")

        for i in range(len(self.stack) - 1, -1, -1):
            print(self.stack[i])

    # Check empty
    def isEmpty(self):
        return len(self.stack) == 0


s = Stack()


while True:

    print("\n----- STACK MENU -----")
    print("1. Push")
    print("2. Pop")
    print("3. Peek")
    print("4. Display")
    print("5. Check if Empty")
    print("6. Exit")

    choice = int(input("Enter your choice: "))

    if choice == 1:

        data = int(input("Enter data: "))
        s.push(data)
        print("Element pushed successfully.")

    elif choice == 2:

        element = s.pop()

        if element is not None:
            print("Popped element:", element)

    elif choice == 3:

        s.peek()

    elif choice == 4:

        s.display()

    elif choice == 5:

        if s.isEmpty():
            print("Stack is empty")
        else:
            print("Stack is not empty")

    elif choice == 6:

        print("Program terminated.")
        break

    else:

        print("Invalid choice. Please try again.")