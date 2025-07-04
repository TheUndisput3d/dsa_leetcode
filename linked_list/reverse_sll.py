from singly_linked_list import SinglyLinkedList, Node

def reverse_ll(sll):
    stack = []
    temp = sll.head

    while temp != None:
        stack.append(temp.val)
        temp = temp.next

    temp = sll.head
    while temp != None:
        temp.val = stack.pop()
        temp = temp.next

    return sll


def reverse_ll_optimal(sll):
    prev_node = None
    curr = sll.head
    
    while curr is not None:
        front = curr.next  # Move before updating links
        curr.next = prev_node
        prev_node = curr
        curr = front  # Move to the next node

    sll.head = prev_node  # Fix: Update head properly
    return sll

if __name__ == "__main__":
    ll = SinglyLinkedList()
    ll.append(5)
    ll.append(6)
    ll.append(7)
    ll.append(510)

    ll.insert(69, 5)
    # ll.delete(510)
    ll.insert(255, 2)
    ll.insert(35, 3)
    # ll.delete(5)
    print(f"before reversal: ")
    ll.traversal()
    sll = reverse_ll_optimal(ll)
    print(f"after reversal: ")
    sll.traversal()
