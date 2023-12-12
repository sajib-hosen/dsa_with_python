
# date: 10.12.2023
# name: sajib hosen
# email: sajib.201h@gamil.com

# DUBLY LINKED_LIST 
# Advantages of Doubly Linked List over the singly linked list:
#    A DLL can be traversed in both forward and backward directions. 
#    The delete operation in DLL is more efficient if a pointer to the node to be deleted is given. 
#    We can quickly insert a new node before a given node. 
#    In a singly linked list, to delete a node, a pointer to the previous node is needed. To get this previous node, sometimes the list is traversed. In DLL, we can get the previous node using the previous pointer. 

# Disadvantages of Doubly Linked List over the singly linked list:
#    Every node of DLL Requires extra space for a previous pointer. It is possible to implement DLL with a single pointer though (See this and this). 
#    All operations require an extra pointer previous to be maintained. For example, in insertion, we need to modify previous pointers together with the next pointers. For example in the following functions for insertions at different positions, we need 1 or 2 extra steps to set the previous pointer.

# Applications of Doubly Linked List:
#    It is used by web browsers for backward and forward navigation of web pages 
#    LRU ( Least Recently Used ) / MRU ( Most Recently Used ) Cache are constructed using Doubly Linked Lists. 
#    Used by various applications to maintain undo and redo functionalities. 
#    In Operating Systems, a doubly linked list is maintained by thread scheduler to keep track of processes that are being executed at that time.

# Ref >> https://www.geeksforgeeks.org/data-structures/linked-list/doubly-linked-list/ 

class Node:
    def __init__(self, data) -> None:  # Function to initialize the node object
        self.prev = None # Initialize nes
        self.data = data # Assign data
        self.next = None # Initialize # next as null


class DublyLinkedList:
    def __init__(self) -> None:
        self.head = None
        self.tail = None
        self.previous_node = None

    #print the list
    def printF(self):
        temp = self.head
        while (temp):
            print(temp.data, end=" ")
            temp = temp.next
        print("_")

    #print out the list 
    def push(self, data):
        new_node = Node(data)
        last_node = self.head
        if(not self.head):
            self.head = new_node
        else:
            while(last_node):
                if(not last_node.next):
                    break
                else:
                    last_node = last_node.next
            last_node.next = new_node
            new_node.prev = last_node

    #push at the start of list
    def unshift(self, data):
        new_node = Node(data)
        self.head.prev = new_node
        new_node.next = self.head
        self.head = new_node

    #return the value of an specific index
    def get_by_index(self, index):
        index_count = 0
        current_node = self.head
        while(current_node):
            if(index_count == index):
                return current_node.data
            else:
                current_node = current_node.next
                index_count += 1

    #delete the last item of the list
    def pop(self):
        second_last = self.head
        value = None
        if(not self.head.next):
            value = second_last.data
            del second_last
            self.head = None
        else:
            while(second_last):
                if(not second_last.next.next):
                    value = second_last.next.data
                    del second_last.next
                    second_last.next = None
                    break
                else:
                    second_last = second_last.next
        return value
    
    #delete by index number
    def delete_at(self, index:int):
        current_index = 0
        current_node = self.head
        self.previous_node = None
        if(index == 0):
            self.head = current_node.next
            del current_node
        else:
            while(current_node):
                if(current_index == index):
                    next_node = None
                    if(current_node.next):
                        next_node = current_node.next
                        next_node.prev = self.previous_node
                    else:
                        self.previous_node.next = next_node
                        del current_node
                    break
                else:
                    self.previous_node = current_node
                    current_node = current_node.next
                    current_index += 1
        self.previous_node = None

    #return the length of list
    def length(self):
        index_cound = 0
        temp = self.head
        while(temp):
            index_cound += 1
            temp = temp.next
        return index_cound

    #revers the list
    def revers_list(self):
        pass
        


if __name__=='__main__':
    Dlist = DublyLinkedList()  #defining and empty location in memory
    # Dlist.head = Node(1) #defining individual node and assigning it to linked_list head
    # print("pop return  >>", Dlist.pop())

    Dlist.push(1)
    print("pop return >>", Dlist.pop())
    Dlist.push(2)
    Dlist.push(4)
    Dlist.push(3)
    print("pop return >>", Dlist.pop())
    Dlist.push(5)

    print('before delete')
    Dlist.printF()

    Dlist.delete_at(0)
    print('after delete')
    Dlist.printF()

    # Dlist.pop()
    # Dlist.push(5)
    # Dlist.unshift(-2)
    # Dlist.printF()
    # print("len >>", Dlist.length())
    # print("at >>", Dlist.get_by_index(0))


   