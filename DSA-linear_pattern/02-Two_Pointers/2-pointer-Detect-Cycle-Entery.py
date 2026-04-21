class LinkedNode:
    def __init__ (self, value:int = 0 , next:'LinkedNode | None' = None):
        self.value = value
        self.next = next

def detect_cycle_entry(head:'LinkedNode | None') -> 'LinkedNode | bool | None':
    """
    find the point where the cycle begins in a linked list.
    Pattern: Fast and Slow Pointers.
    """
    if not head:
        return None
    
    slow = fast = head

    # phase 1: Detect the cycle
    while fast and fast.next and slow:
        slow = slow.next
        fast = fast.next.next
        if slow == fast:
            break
    else:   # this else block executes if the while loop is not broken (since belongs to while), meaning no cycle.
        return False
    
    # phase 2: find the entry point
    slow = head
    while slow != fast and slow and fast:
        slow = slow.next
        fast = fast.next
    
    return slow

if __name__ == "__main__":
    # Creating a linked list with a cycle for testing
    node1 = LinkedNode(3)
    node2 = LinkedNode(2)
    node3 = LinkedNode(0)
    node4 = LinkedNode(-4)

    node1.next = node2
    node2.next = node3
    node3.next = node4
    node4.next = node2  # Creates a cycle here

    entry_node = detect_cycle_entry(node1)
    if entry_node:
        print(f"Cycle detected at node with value: {entry_node.value}")
    else:
        print("No cycle detected.")
