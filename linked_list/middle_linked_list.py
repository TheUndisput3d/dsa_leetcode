from singly_linked_list import SinglyLinkedList, Node

def find_middle(sll):
    n = 0 # init the len of ll to be 0 at first
    curr = sll.head
    while curr != None:
        curr = curr.next
        n += 1
    print(n)
    curr = sll.head
    for _ in range(n//2):
        curr = curr.next
    print(f"middle value is {curr.val}")

def find_optimal_middle(sll):
    sp = fp = sll.head

    while fp != None and fp.next != None:
        sp = sp.next
        fp = fp.next.next

    return sp.val



if __name__ == "__main__":
    llo = SinglyLinkedList()
    llo.append(5)
    llo.append(6)
    llo.append(7)
    llo.append(510)

    llo.insert(69, 5)
    llo.insert(255, 2)
    llo.insert(35, 3)
    llo.insert(34, 3)
    llo.insert(98, 3)
    llo.traversal()
    find_middle(llo)
    print(find_optimal_middle(llo))
