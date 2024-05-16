class Node:
    def __init__(self, data=None):
        # Initialize a node with data and a reference to the next node
        self.data = data
        self.next = None

def append_to_end(head, data):
    # Append a new node with given data to the end of the list
    if not head:
        # If the list is empty, create a new node and make it the head
        return Node(data)
    current = head
    # Traverse the list until the last node
    while current.next:
        current = current.next
    # Append the new node to the last node's next reference
    current.next = Node(data)
    # Return the head of the list
    return head

def prepend_to_start(head, data):
    # Prepend a new node with given data to the start of the list
    new_node = Node(data)
    # Make the new node point to the current head
    new_node.next = head
    # Update the head to the new node
    return new_node

def delete_node(head, data):
    # Delete the node with given data from the list
    if head is None:
        # If the list is empty, return None
        return None
    if head.data == data:
        # If the node to be deleted is the head, update head to the next node
        return head.next
    current = head
    # Traverse the list until the node before the one to be deleted
    while current.next:
        if current.next.data == data:
            # Update the current node's next reference to skip the node to be deleted
            current.next = current.next.next
            # Return the head of the list
            return head
        current = current.next
    # Return the head of the list
    return head

def print_list(head):
    # Print the elements of the list
    current = head
    while current:
        # Traverse the list and print each node's data
        print(current.data, end=" -> ")
        current = current.next
    # Print None to indicate the end of the list
    print("None")

# Example usage:
if __name__ == "__main__":
    head = None
    # Create an empty linked list
    head = append_to_end(head, 1)
    # Append nodes to the list
    head = append_to_end(head, 2)
    head = append_to_end(head, 3)
    head = append_to_end(head, 4)
    # Print the list
    print_list(head)  # Output: 1 -> 2 -> 3 -> 4 -> None
    # Prepend a node to the list
    head = prepend_to_start(head, 0)
    # Print the list
    print_list(head)  # Output: 0 -> 1 -> 2 -> 3 -> 4 -> None
    # Delete a node from the list
    head = delete_node(head, 2)
    # Print the list
    print_list(head)  # Output: 0 -> 1 -> 3 -> 4 -> None
