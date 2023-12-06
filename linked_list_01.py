

# date: 06.12.2023
# name: sajib hosen - email: sajib.201h@gamil.com
# ref: https://www.geeksforgeeks.org/python-data-structures-and-algorithms/

# LINKED_LIST 
# A linked list is a "linear data" structure, in which the elements are not stored at contiguous memory locations. The elements in a linked list are linked using pointers as shown in the below image:

# A linked list is represented by a pointer to the first node of the linked list. The first node is called the head. If the linked list is empty, then the value of the head is NULL. Each node in a list consists of at least two parts:
#   1 Data
#   2 Pointer (Or Reference) to the next node


class Node:
    def __init__(self, data) -> None:  # Function to initialize the node object
        self.data = data # Assign data
        self.next = None # Initialize # next as null

class LinkedList:
    def __init__(self) -> None:
        self.head = None
        self.preNode = None

    def print_list(self):
        temp = self.head
        text_list = ''
        while (temp):
            text_list = text_list + f' {temp.data}'
            temp = temp.next
        print(text_list, "_")

    def push(self, data):
        lastNode = self.head
        new_node = Node(data)
        while(lastNode): # finding the last index
            if(not lastNode.next):
                break
            else:
                lastNode = lastNode.next
        lastNode.next = new_node # assigning the new node to last next

    def unshipt(self, data):
        pass

    def insert_at(self, data, index):
        pass

    def delete_value(self, data):
        currentNode = self.head
        isHead = True
        self.preNode = None
        while(currentNode):
            if(currentNode.data == data):
                if(isHead):
                    self.head = currentNode.next
                    isHead = False
                else:
                    self.preNode.next = currentNode.next
                del currentNode
                break
            else:
                self.preNode = currentNode
                currentNode = currentNode.next
            isHead = False

    def delete_index(self, index):
        self.preNode = None
        currentNode = self.head
        currentIndex = 0
        while(currentNode):
            if(currentIndex == index):
                if(currentIndex == 0):
                    self.head = currentNode.next
                else:
                    self.preNode.next = currentNode.next
                del currentNode
                break
            currentNode = currentNode.next
            currentNode =+ 1





if __name__=='__main__':

    llist = LinkedList()  #defining and empty location in memory
    llist.head = Node(1) #defining individual node and assigning it to linked_list head
    second = Node(2) #defining individual node
    third = Node(3) #defining individual node
    llist.head.next = second
    second.next = third
    #              1    2    3
    # print(llist.head.next.next.data)

    llist.push(4)
    llist.push(5)
    llist.push(6)

    # added data 
    print('item added')
    llist.print_list()

    print('after delete')
    llist.delete_value(6)
    llist.print_list()

