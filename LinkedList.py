class Node:
    def __init__(self, data=None, next=None):

        # The data is the value that is to be enterd
        self.data = data
        
        # The "next" is the value or memory address for the next element
        self.next = next

class LinkedList:
    
    def __init__(self):
        # Head is the first element of the linkedList
        self.head = None

    def printLinkedList(self):
    
        # This if statement checks if the head is null, ie,
        # if the first value of the list is null then it means 
        # that the given list is empty
        if self.head is None:
            print("Linked list is empty")
            return
    
        # itr is the first element of the linkedlist
        itr = self.head
    
        # llstr is an empty string where we can add the data(value) 
        # of the head of ll(Linked List)
        llstr = ''
    
        # This loops for every node and adds the data part of node to llstr
        while itr:
            llstr += str(itr.data)+' --> ' if itr.next else str(itr.data)
            itr = itr.next
    
        # Simply printing the linked list(only data)
        print(llstr)


    def get_length(self):

        # Starting count with 0 as it counts the number of elements of the ll
        count = 0
        
        # itr is assigned as the head or the first element of the ll
        itr = self.head

        # iterating for every element and incrementing the value of count by 1
        while itr:
            count+=1
            itr = itr.next

        return count


    def insert_at_begining(self, data):

        # Creating a new node. The "next" value is self.head becasue the 1st 
        # number is changed to 2nd element.
        node = Node(data, self.head)
        
        # Assignin the newly created node to the head ie,
        # to the first element of the ll
        self.head = node

    def insert_at_end(self, data):

        # Checking if head is null.
        # if head is null then the head will be the data provided
        if self.head is None:
            self.head = Node(data, None)
            return

        # assiging itr as the first elemnt
        itr = self.head

        # simple loop to reach till the end of the list
        while itr.next:
            itr = itr.next
        
        # once the last element is reached the next node is created 
        # the value is data given and since it is the last node so 
        # there will be no memory address.
        itr.next = Node(data, None)

    # Not so sure for inserting values at points except 0
    def insert_at(self, index, data):

        # Checking if the index is invalid ie if is a -Z
        # or out of bounds
        if index<0 or index>self.get_length():
            raise Exception("Invalid Index")

        # Using the insert_at_begining if the index is 0
        if index==0:
            self.insert_at_begining(data)
            return

        # starting the count with 0
        count = 0

        # Assigning itr as first element of the list
        itr = self.head

        # iterating through the list
        while itr:

            # if the count is 1 less than index we create a new node
            # the value will be the given data and the address for the next node will be
            # itr.next. Changing the next node to node
            if count == index - 1:
                node = Node(data, itr.next)
                itr.next = node
                break

            itr = itr.next
            count += 1

    def remove_at(self, index):
        # Checking if the index is valid or not
        if index<0 or index>=self.get_length():
            raise Exception("Invalid Index")

        # if the index is 0 then the first element can be changed 
        # to the second elemnt of the list
        if index==0:
            self.head = self.head.next
            return

        # Starting count as 0
        count = 0

        # assgining itr as the first element of the list
        itr = self.head

        # looping through the entire list
        while itr:

            # if the count is 1 less than index then the next element 
            # is changed to the next to next element. Thus deleting the 
            # next element

            if count == index - 1:
                itr.next = itr.next.next
                break

            itr = itr.next
            count+=1
    
    def insert_values(self, data_list):
        # Clearing the entire ll if any
        self.head = None

        # looping through the array and adding 
        # every element using insert_at_end() method
        for data in data_list:
            self.insert_at_end(data)


if __name__ == '__main__':
    ll = LinkedList()
    ll.insert_values(["banana","mango","grapes","orange"])
    ll.insert_at(1,"blueberry")
    ll.remove_at(2)
    ll.printLinkedList()

    ll.insert_values([45,7,12,567,99])
    ll.insert_at_end(67)
    ll.printLinkedList()
()
# COMPLETE #