from singly_linked_list import SinglyLinkedList


def length_loop_ll(ll):
    my_dict = {}
    curr = ll.head
    travelledLength = 0
    while curr is not None:
        if curr in my_dict:
            return travelledLength - my_dict[curr]
        my_dict[curr] = travelledLength
        travelledLength += 1
        curr = curr.next
    return None

def length_loop_ll_optimal(ll):
    slow = fast = ll.head
    while fast is not None and fast.next is not None:
        slow = slow.next
        fast = fast.next.next
        if slow == fast:
            slow = slow.next
            length = 1
            while slow != fast:
                length += 1
                slow = slow.next
            return length
    return None


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
    ll.traversal()

    curr = ll.head

    while curr.next is not None:
        curr = curr.next
    
    curr.next = ll.head


    print(length_loop_ll_optimal(ll))