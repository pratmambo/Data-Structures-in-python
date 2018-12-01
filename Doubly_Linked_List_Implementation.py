class Node(object):

    def __init__(self, value):                         # node with three parts, 2 pointers to nodes(previous and next) and 1 data part
        self.prevNode = None
        self.value = value
        self.nextNode = None


class DoublyLinkedList(object):

    def __init__(self):
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
        if self.head is None:
            newNode = Node(value)
            self.head = newNode
        else:
            newNode = Node(value)
            self.head.prevNode = newNode
            newNode.nextNode = self.head
            self.head = newNode

    def insertAtEnd(self, value):
        if self.size() == 0:
            self.insertAtBeginning(value)
        else:
            newNode = Node(value)
            temp = self.head
            while temp.nextNode is not None:      # Looping till the last node
                temp = temp.nextNode
            temp.nextNode = newNode
            newNode.prevNode = temp

    def insertAtPosition(self, value, position):
        if 0 <= position <= self.size():
            if position == 0:
                self.insertAtBeginning(value)
            elif position == self.size():
                self.insertAtEnd(value)
            else:
                temp = self.head
                newNode = Node(value)
                for i in range(position):  # Looping till the node that is 1 less than the given position
                    temp = temp.nextNode
                prevNode = temp.prevNode
                prevNode.nextNode = newNode
                newNode.prevNode = prevNode
                newNode.nextNode = temp
                temp.prevNode = newNode

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

    def deleteAtBeginning(self):
        if self.size() > 0:
            if self.size() == 1:
                self.head = self.head.nextNode
            else:
                self.head = self.head.nextNode
                del self.head.prevNode
                self.head.prevNode = None

    def deleteAtEnd(self):
        if self.size() > 0:
            if self.size() == 1:
                self.deleteAtBeginning()
            else:
                temp = self.head
                while temp.nextNode is not None:
                    temp = temp.nextNode
                temp.prevNode.nextNode = None
                del temp

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
                        temp.nextNode.prevNode = previous  # setting the next nodes' prevNode pointer to previous node
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
                        temp.nextNode.prevNode = previous
                        return
                    previous = temp
                    temp = temp.nextNode
                    count += 1                          # count value increases for every node visited

                previous.nextNode = temp.nextNode
                return
        raise ValueError("Size of linked list is: " + str(self.size()))  # raising error if position is not valid

    def printList(self):  # prints the linked list by traversing all nodes
        if self.size() > 0:
            temp = self.head
            while temp.nextNode is not None:
                print(temp.value, end=" ")
                temp = temp.nextNode
            print(temp.value)
        else:
            print(None)

    def printRevList(self):  # prints the linked list in reverse order
        if self.size() > 0:
            temp = self.head
            while temp.nextNode is not None:
                temp = temp.nextNode
            while temp.prevNode is not None:
                print(temp.value, end=" ")
                temp = temp.prevNode
            print(temp.value)
        else:
            print(None)


nums = DoublyLinkedList()
nums.insertAtBeginning(3)
nums.printList()
nums.printRevList()
nums.insertAtBeginning(2)
nums.printList()
nums.printRevList()
nums.insertAtBeginning(1)
nums.printList()
nums.printRevList()
nums.insertAtEnd(4)
nums.printList()
nums.printRevList()
nums.deleteAtPosition(3)
nums.printList()
nums.printRevList()