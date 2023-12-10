
# date: 10.12.2023
# name: sajib hosen
# email: sajib.201h@gamil.com

# DUBLY LINKED_LIST 



class Node:
    def __init__(self, data) -> None:  # Function to initialize the node object
        self.prev = None # Initialize nes
        self.data = data # Assign data
        self.next = None # Initialize # next as null


class DublyLinkedList:
    def __init__(self) -> None:
        self.head = None

    def printF(self):
        temp = self.head
        while (temp):
            print(temp.data, end=" ")
            temp = temp.next
        print("_")

    # print out the list 
    def push(self, data):
        new_node = Node(data)
        last_node = self.head
        while(last_node):
            if(not last_node.next):
                break
            else:
                last_node = last_node.next
        last_node.next = new_node

    def unshift(self, data):
        pass

    def get_by_index(self, index):
        pass

    def pop(self):
        second_last = self.head
        while(second_last):
            if(not second_last.next.next):
                del second_last.next
                second_last.next = None
                break
            else:
                second_last = second_last.next
    
    def delete_at(self, index):
        pass

    def length(self):
        index_cound = 0
        temp = self.head
        while(temp):
            index_cound += 1
            temp = temp.next
        return index_cound

    def revers_list(self):
        pass
        


if __name__=='__main__':
    Dlist = DublyLinkedList()  #defining and empty location in memory
    Dlist.head = Node(1) #defining individual node and assigning it to linked_list head

    Dlist.push(2)

    Dlist.push(3)
    Dlist.push(4)

    Dlist.printF()

    Dlist.pop()
    Dlist.push(5)
    Dlist.printF()
    print("len >>", Dlist.length())


   