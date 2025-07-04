class Node:
    def __init__(self, val):
        self.val = val
        self.next = None    

class SinglyLinkedList:
    def __init__(self):
        self.head = None

    def append(self, val):
        new_node = Node(val)
        if self.head is None:
            self.head = new_node
        else:
            curr = self.head
            while curr.next != None:
                curr = curr.next
            curr.next = new_node


    def traversal(self):
        if self.head == None:
            print("SLL is empty.")

        else:
            curr = self.head
            while curr != None:
                print(curr.val, end=" ")
                curr = curr.next
            print()

    def insert(self, val, ind):
        new_node = Node(val)
        if not ind:
            new_node.next = self.head
            self.head = new_node
            return 
        curr = self.head
        prev_node = None
        count = 0
        while curr != None and count < ind:        
            prev_node = curr
            curr = curr.next
            count += 1
        prev_node.next = new_node
        new_node.next = curr

    def delete(self, val=None):
        """
        Deletes the first node by default when no arguments are passed. 
        """
        temp = self.head
        if not val:
            self.head = self.head.next
            temp.next = None # this step is redundant can use del without doing this
            del temp # can directly delete without previous step. and can totally skip these 2 steps aswell
            return  
        prev_node = None

        while temp is not None and temp.val != val:
            prev_node = temp
            temp = temp.next

        if not temp: # edge case when trying to delete a value not present in the ll
            print(f"Not found value: {val}")
            return  

        prev_node.next = temp.next
        temp.next = None
        del temp


    
    # def delete(self, val=None):
    #     """
    #     Deletes the first node by default when no arguments are passed. 
    #     """
    #     temp = self.head
    #     if not val:
    #         self.head = self.head.next
    #         temp.next = None # this step is redundant can use del without doing this
    #         del temp # can directly delete without previous step. and can totally skip these 2 steps aswell
    #         return  
    #     prev_node = None

    #     while temp is not None and temp.val != val:
    #         prev_node = temp
    #         temp = temp.next

    #     if not temp: # edge case when trying to delete a value not present in the ll
    #         print(f"Not found value: {val}")
    #         return  

    #     prev_node.next = temp.next
    #     temp.next = None
    #     del temp

    def delete(self, val=None):
        """
        Deletes the first node by default when no arguments are passed. 
        """
        temp = self.head
        if not val or temp.val == val:
            self.head = self.head.next
            temp.next = None # this step is redundant can use del without doing this
            del temp # can directly delete without previous step. and can totally skip these 2 steps aswell
            return  
        prev_node = None
        found = False
        while temp:
            if temp.val == val: 
                found = True
                break
            prev_node = temp
            temp = temp.next
        
        if found:
            prev_node.next = temp.next
            temp.next = None
            del temp
        else:
            print(f"Node with value {val} not found")
        
print(__name__)




if __name__ == "__main__":
    ll = SinglyLinkedList()
    ll.append(5)
    ll.append(6)
    ll.append(7)
    ll.append(510)

    ll.insert(69, 5)
    ll.delete(510)
    ll.insert(255, 2)
    ll.insert(35, 3)
    ll.delete(5)


