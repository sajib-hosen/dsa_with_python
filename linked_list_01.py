
# date: 06.12.2023
# name: sajib hosen
# email: sajib.201h@gamil.com

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

    # print out the list 
    def print_list(self):
        temp = self.head
        text_list = ''
        while (temp):
            text_list = text_list + f' {temp.data}'
            temp = temp.next
        print(text_list, "_")

    # return the length of the list 
    def length(self):
        index_count = 0
        currentNode = self.head
        while(currentNode):
            index_count += 1
            if(not currentNode.next):
                break
            else:
                currentNode = currentNode.next
        return index_count
    
    # if value exist return the index
    def is_exist(self, data):
        index_count = 0
        currentNode = self.head
        while(currentNode):
            if(currentNode.data == data):
                return index_count
            currentNode = currentNode.next
            index_count += 1
        return None

    # insert a value at the end of list
    def push(self, data):
        lastNode = self.head
        new_node = Node(data)
        while(lastNode): # finding the last index
            if(not lastNode.next):
                break
            else:
                lastNode = lastNode.next
        lastNode.next = new_node # assigning the new node to last next

    # insert a value at beginning of the list
    def unshipt(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

    # insert a value at a specific position
    def insert_at(self, data, index=None):
        self.preNode = None
        current_index = 0
        currentNode = self.head
        while(currentNode):
            if(data and not index):
                self.push(data)
                break
            else:
                if(current_index == index):
                    if(index == 0):
                        self.unshipt(data)
                    else:
                        new_node = Node(data)
                        new_node.next = currentNode
                        self.preNode.next = new_node
                    break
                else:
                    self.preNode = currentNode
                    currentNode = currentNode.next
                    current_index += 1

    # delete a value but the value
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

    # delete a value by index
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
            self.preNode = currentNode
            currentNode = currentNode.next
            currentIndex += 1

    # reverse the list
    def reverse_list(self):
        pass


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

    print('item added')
    llist.print_list()

    print('after delete')
    llist.delete_value(6)
    llist.delete_index(4)

    print('after unshift')
    llist.unshipt(0)
    llist.print_list()

    # print('length >>', llist.length())
    
    llist.insert_at(12, 2)
    print('length >>', llist.length())
    llist.print_list()

    print('is exist at', llist.is_exist(3))


# thanks for helping out me : https://www.geeksforgeeks.org/python-data-structures-and-algorithms/