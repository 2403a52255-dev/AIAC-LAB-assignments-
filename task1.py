class Stack:
    """A Stack implementation using a list with LIFO (Last-In-First-Out) behavior.

    Attributes:
        items (list): The list storing the stack elements.
    """
    def __init__(self, initial_array=None):
        """Initialize stack with optional initial array.
        Args:
            initial_array (list, optional): Initial array to populate the stack.
        """
        self.items = []
        if initial_array:
            for item in initial_array:
                self.push(item)
    def push(self, item):
        """Push an item onto the stack.
        Args:
            item: The item to be pushed.
        """
        self.items.append(item)
    def pop(self):
        """Remove and return the top item from the stack.
        Returns:
            The top item from the stack.
        Raises:
            IndexError: If stack is empty.
        """
        if not self.is_empty():
            return self.items.pop()
        raise IndexError("Stack is empty")
    def peek(self):
        """Return the top item from the stack without removing it.
        Returns:
            The top item from the stack.
        Raises:
            IndexError: If stack is empty."""
        if not self.is_empty():
            return self.items[-1]
        raise IndexError("Stack is empty")
    def is_empty(self):
        """Check if the stack is empty.
        Returns:
            bool: True if stack is empty, False otherwise."""   
        return len(self.items) == 0
    def __str__(self):
        """Return string representation of the stack.
        Returns:
            str: String representation of stack contents.  """
        return str(self.items)
# Test the implementation
if __name__ == "__main__":
    # Initial array
    initial_array = [3, 5, 8, 9, 6, 1]   
    # Create stack with initial array
    stack = Stack(initial_array)   
    # Test operations
    print("Initial stack:", stack)  
    # Push a new element
    stack.push(7)
    print("After pushing 7:", stack)   
    # Pop an element
    popped_item = stack.pop()
    print(f"Popped item: {popped_item}")
    print("After popping:", stack) 
    # Peek at top element
    top_item = stack.peek()
    print(f"Top item (peek): {top_item}") 
    # Check if empty
    print("Is stack empty?", stack.is_empty())