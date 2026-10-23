"""     Yanci Hernandez     CMSC 315
===========================================================
UNIT 2 DISCUSSION: STACKS AND QUEUES (PYTHON)
===========================================================

OVERVIEW:
This assignment introduces two fundamental data structures:
the Stack (LIFO) and the Queue (FIFO).

You will complete, modify, and extend the starter code while
explaining key concepts through comments and improved output.
"""

from collections import deque


class Stack:
    def __init__(self):
        # TODO (Student): Create the internal data structure for the stack.
        # Hint: using a standard Python list to store stack values.
        self.items= []


    def push(self, value):
        # TODO (Student): Add value to the stack.
        # Add a short comment explaining why this operation supports LIFO behavior.
        # new items are appended/added to end of list; a pop() operation will remove this newly
          # item first; this cycle creates LIFO
        self.items.append(value)

    def pop(self):
        # TODO (Student): Remove and return the most recently added value.
        # Improve or explain empty-stack handling.
        # What should happen if the stack is empty? It s/ return None to avoid IndexError
        if self.is_empty():
            print("[Warning] Attempted to pop from an empty stack!")
            return None
        # otherwise, remove and return the top (or last added) item
        return self.items.pop()
        #pass

    def peek(self):
        # TODO (Student): Return the top value without removing it.
        # Add a comment explaining what peek does = displays the last added item w/o removing it
        if self.is_empty():
            print("[Warning] Attempted to peek at an empty stack!")
            return None
        return self.items[-1]

    def is_empty(self):
        # TODO (Student): Returns True if the stack has no values left on the list.
        return len(self.items) == 0


class Queue:
    def __init__(self):
        # TODO (Student): Create the internal data structure for the queue.
        # Hint: collections.deque is useful for efficient queue operations.
        self.items = deque()

    def enqueue(self, value):
        # TODO (Student): Add value to the back of the queue.
        # Add a short comment explaining why this operation supports FIFO behavior.
        # new items added to back of Q but taken from the front = FIFO behavior
        self.items.append(value)

    def dequeue(self):
        # TODO (Student): Remove and return the value from the front of the queue.
        # Explain or improve empty-queue handling.
        # If the queue is empty, return None to handle it gracefully.
        if self.is_empty():
            print("[Warning] Attempted to dequeue from an empty queue!")
            return None
        # Remove and return the front (leftmost) item of the queue.
        return self.items.popleft()

    def front(self):
        # TODO (Student): Return the front value without removing it.
        # Add a comment explaining what front returns.
        if self.is_empty():
            print("[Warning] Attempted to view the front of an empty queue!")
            return None
        # Returns the front item of the queue (at index 0) without removing it.
        return self.items[0]

    def is_empty(self):
        # TODO (Student): Return True if the queue has no values.
        # Returns True if the queue has no elements.
        return len(self.items) == 0


    def test_peek_multiple_tickets(self):
        """
        Verify that viewing the front multiple times does not remove items from the queue.
        """
        print("\n--- Running test_peek_multiple_tickets ---")

        # Add test items to this queue
        self.enqueue('A')
        self.enqueue('B')
        self.enqueue('C')

        # Peek multiple times; the front should remain A
        print(f"Peek 1: {self.front()}")
        print(f"Peek 2: {self.front()}")
        print(f"Peek 3: {self.front()}")

        # Remove the first item to confirm FIFO behavior
        print(f"Dequeued item: {self.dequeue()}")
        print(f"New front: {self.front()}")

        # Clear remaining items so the queue is empty
        while not self.is_empty():
            self.dequeue()



def main():
    print("=== UNIT 2: STACKS AND QUEUES ===")

    # ===============================
    # TODO (Student): STACK DEMO
    # ===============================
    # Requirements:
    # 1. Create a Stack object.
    # 2. Add at least 4 values to the stack.
    # 3. Improve the print statements so they clearly explain what is happening.
    # 4. Demonstrate LIFO behavior.
    # 5. Show what happens when pop() is used on an empty stack.
    #
    # Edge Cases:
    # 6. Show what happens when peek() is used on an empty stack.
    # 7. Create a stack with only one item, remove it,
    #    and verify the stack is empty afterward.


    print("\n=== STACK DEMO ===")
    print("TODO: Create a Stack object, demonstrate LIFO behavior,")
    print("      test popping from an empty stack,")
    print("      test peeking at an empty stack,")
    print("      and verify a single-item stack becomes empty after removal.")

# creation of Stack object
    my_stack = Stack()

# 1. Edge Case: Peek and Pop on empty stack
    print("Checking empty stack edge cases...")
    print(f"Peek empty stack: {my_stack.peek()}")
    print(f"Pop empty stack: {my_stack.pop()}")

# 2. Add at least 4 values to the stack
    print("\nPushing elements: 10, 20, 30, 40")
    my_stack.push(10)
    my_stack.push(20)
    my_stack.push(30)
    my_stack.push(40)

# 3. Demonstrate LIFO behavior
    print(f"Current top (peek): {my_stack.peek()}")
    print("Popping elements to verify LIFO order:")
    while not my_stack.is_empty():
        print(f"Popped: {my_stack.pop()}")

# 4. Single item edge case
    print("\nTesting single-item stack behavior:")
    my_stack.push(99)
    print(f"Stack is_empty after push(99)? {my_stack.is_empty()}")
    print(f"Popping single item: {my_stack.pop()}")
    print(f"Stack is_empty after pop? {my_stack.is_empty()}")


# ===============================
# TODO (Student): QUEUE DEMO
# ===============================
# Requirements:
# 1. Create a Queue object.
# 2. Add at least 4 values to the queue.
# 3. Improve the print statements so they clearly explain what is happening.
# 4. Demonstrate FIFO behavior.
# 5. Show what happens when dequeue() is used on an empty queue.
#
# Edge Cases:
# 6. Show what happens when front() is used on an empty queue.
# 7. Create a queue with only one item, remove it,
#    and verify the queue is empty afterward.

    print("\n=== QUEUE DEMO ===")
    print("TODO: Create a Queue object, demonstrate FIFO behavior,")
    print("      test dequeuing from an empty queue,")
    print("      test viewing the front of an empty queue,")
    print("      and verify a single-item queue becomes empty after removal.")

# creation of Q object
    my_queue = Queue()

# 1. Edge Case: Front and Dequeue on empty queue
    print("Checking empty queue edge cases...")
    print(f"Front of empty queue: {my_queue.front()}")
    print(f"Dequeue from empty queue: {my_queue.dequeue()}")

# 2. Add at least 4 values to the queue
    print("\nEnqueuing elements: 'A', 'B', 'C', 'D'")
    my_queue.enqueue('A')
    my_queue.enqueue('B')
    my_queue.enqueue('C')
    my_queue.enqueue('D')

# 3. Demonstrate FIFO behavior
    print(f"Current front: {my_queue.front()}")
    print("Dequeuing elements to verify FIFO order:")
    while not my_queue.is_empty():
        print(f"Dequeued: {my_queue.dequeue()}")

# 4. Single item edge case
    print("\nTesting single-item queue behavior:")
    my_queue.enqueue('Z')
    print(f"Queue is_empty after enqueue('Z')? {my_queue.is_empty()}")
    print(f"Dequeuing single item: {my_queue.dequeue()}")
    print(f"Queue is_empty after dequeue? {my_queue.is_empty()}")

    # run multiple peek test
    my_queue = Queue()
    my_queue.test_peek_multiple_tickets()

if __name__ == "__main__":
    main()
