class Node(object):

    def __init__(self, value):                    # Creating a node with given data or value and a pointer to next node
        self.value = value                        # initializing data or value to user given data
        self.nextNode = None                      # initializing pointer to None


class SinglyLinkedList(object):
    def __init__(self):                           # Creating an empty linked list with head pointing to None
        self.head = None

    def size(self):
        if self.head is None:                     # Check if head points to None and if so list is empty
            return 0
        else:
            count = 0
            temp = self.head
            while temp.nextNode is not None:      # Looping till last node as last node's pointer is None
                count += 1
                temp = temp.nextNode
            count += 1
            return count

    def insertAtBeginning(self, value):
        newNode = Node(value)                     # Creating a new node
        newNode.nextNode = self.head              # Setting the new nodes pointer to head(even if head points to None, even then it fits)
        self.head = newNode                       # Setting head to the new node as it is the first node

    def insertAtEnd(self, value):
        if self.head is None:                     # if head is None the inserting at end is same as inserting in the beginning
            self.insertAtBeginning(value)
        else:
            newNode = Node(value)
            temp = self.head
            while temp.nextNode is not None:      # Looping till last node as last node's pointer is None
                temp = temp.nextNode
            temp.nextNode = newNode

    def insertAtPosition(self, value, position):
        if 0 <= position <= self.size():             # Checking if position is present
            if position == 0:
                self.insertAtBeginning(value)
            elif position == self.size():
                self.insertAtEnd(value)
            else:
                temp = self.head
                newNode = Node(value)
                for i in range(position-1):           # Looping till the node that is 1 less than the given position
                    temp = temp.nextNode
                nodeAtPos = temp.nextNode             # Storing the address of node that is currently at the given position
                temp.nextNode = newNode
                newNode.nextNode = nodeAtPos

    def find(self, value):                            # returns position of value from 0 and if not found returns -1
        temp = self.head
        if self.size() == 1:
            if temp.value == value:                   # if value is found in the first node
                return 0
            else:
                return -1
        else:
            count = 0
            while temp.nextNode is not None:           # Looping till the last node and checking each node for value
                if temp.value == value:
                    return count
                else:
                    temp = temp.nextNode               # if value is not found changing temp to the next node on list
                    count += 1
            if temp.value == value:                    # checking if last node has required value
                return count
            return -1

    def deleteAtBeginning(self):                      # changing head to next node and deleting the first node
        if self.size() > 0:
            temp = self.head
            del self.head                             # deleting first node from memory
            self.head = temp.nextNode

    def deleteAtEnd(self):
        if self.size() > 0:
            if self.size() == 1:                      # if size of list is 1 the delete at end is same as delete at beginning
                self.deleteAtBeginning()
            else:
                previous = None                       # stores the address of the previous node visited
                temp = self.head
                while temp.nextNode is not None:      # Looping till the last node
                    previous = temp
                    temp = temp.nextNode
                previous.nextNode = None              # setting the nextNode of last but one node to None
                del temp                              # deleting last node from memory

    def deleteValue(self, value):
        if self.size() > 0:
            if self.head.value == value:              # checking if value is present at first position
                self.deleteAtBeginning()
                return
            else:
                previous = self.head
                temp = self.head.nextNode
                while temp.nextNode is not None:      # Looping through the list to find value
                    if temp.value == value:
                        previous.nextNode = temp.nextNode  # setting the previous nodes next pointer to the next pointer of node where value was found
                        del temp
                        return
                    previous = temp
                    temp = temp.nextNode
                if temp.value == value:                 # checking if last node has the required value
                    previous.nextNode = temp.nextNode
                    del temp
                    return
        raise ValueError("Value not in linked list")    # if value is not found

    def deleteAtPosition(self, position):
        if 0 <= position < self.size():                 # checking if given position is valid
            if position == 0:
                self.deleteAtBeginning()
                return
            else:
                count = 1
                previous = self.head
                temp = self.head.nextNode
                while temp.nextNode is not None:        # Looping till the given position by matching count and position
                    if count == position:
                        previous.nextNode = temp.nextNode
                        return
                    previous = temp
                    temp = temp.nextNode
                    count += 1                          # count value increases for every node visited

                previous.nextNode = temp.nextNode
                return
        raise ValueError("Size of linked list is: " + str(self.size()))  # raising error if position is not valid

    def printList(self):                                # prints the linked list by traversing all nodes
        if self.size() > 0:
            temp = self.head
            while temp.nextNode is not None:
                print(temp.value, end=" ")
                temp = temp.nextNode
            print(temp.value)
        else:
            print(None)








