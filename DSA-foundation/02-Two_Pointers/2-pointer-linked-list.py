class ListNode:
    def __init__(self, value:int=0, next: 'ListNode | None' = None):
        self.value = value
        self.next = next

def detect_cycle(head: ListNode) -> bool:
    """Pattern: Fast and Slow Pointers to detect cycle in a linked list."""
    if not head:
        return False
    slow = fast = head

    while fast and fast.next and slow:
        slow = slow.next
        fast = fast.next.next
        if slow == fast:  # compare by the reference not by value*****
            return True
        
    return False

if __name__ == "__main__":
    # Creating a linked list with a cycle for testing
    node1 = ListNode(3)
    node2 = ListNode(2)
    node3 = ListNode(0)
    node4 = ListNode(-4)

    node1.next = node2
    node2.next = node3
    node3.next = node4
    node4.next = node2  # Creates a cycle here

    print(detect_cycle(node1))  # Output: True

    # Creating a linked list without a cycle for testing
    nodeA = ListNode(1)
    nodeB = ListNode(2)

    nodeA.next = nodeB

    print(detect_cycle(nodeA))  # Output: False     