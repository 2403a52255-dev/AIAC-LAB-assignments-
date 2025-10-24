class Node:
    def __init__(self, data):
        self.data = data  # Store the data
        self.next = None  # Initialize the next pointer to None
class LinkedList:
    def __init__(self):
        self.head = None  # Initialize the head of the list to None
    def insert_at_end(self, data):
        new_node = Node(data)  # Create a new node
        if not self.head:  # If the list is empty
            self.head = new_node  # Set the new node as the head
            return
        last_node = self.head  # Start from the head
        while last_node.next:  # Traverse to the last node
            last_node = last_node.next  # Move to the next node
        last_node.next = new_node  # Update the last node's next pointer to the new node
    def delete_value(self, value):
        current_node = self.head  # Start from the head
        if current_node and current_node.data == value:  # Check if the head needs to be deleted
            self.head = current_node.next  # Update head to the next node
            return
        prev_node = None  # Initialize previous node
        while current_node and current_node.data != value:  # Traverse the list
            prev_node = current_node  # Keep track of the previous node
            current_node = current_node.next  # Move to the next node
        if current_node:  # If the value was found
            prev_node.next = current_node.next  # Bypass the current node
    def traverse(self):
        current_node = self.head  # Start from the head
        while current_node:  # Traverse until the end of the list
            print(current_node.data, end=" -> ")  # Print the current node's data
            current_node = current_node.next  # Move to the next node
        print("None")  # Indicate the end of the list
# Test cases with console input
if __name__ == "__main__":
    ll = LinkedList()
    while True:
        action = input("Enter 'insert' to add a value, 'delete' to remove a value, or 'traverse' to display the list (type 'exit' to quit): ").strip().lower()
        if action == 'insert':
            value = int(input("Enter a value to insert: "))
            ll.insert_at_end(value)
        elif action == 'delete':
            value = int(input("Enter a value to delete: "))
            ll.delete_value(value)
        elif action == 'traverse':
            ll.traverse()  # Display the current list
        elif action == 'exit':
            break
        else:
            print("Invalid action. Please try again.")