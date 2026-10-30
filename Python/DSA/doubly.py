class Node:
    def __init__(self, data):
        self.data = data
        self.prev = None
        self.next = None

class DoublyLinkedList:
    def __init__(self):
        self.head = None

    def InsertAtEnd(self, data):
        temp = Node(data)

        if self.head is None:
            self.head = temp
            return

        t = self.head
        while t.next is not None:
            t = t.next

        t.next = temp
        temp.prev = t

    def InsertAtAnyPosition(self, data, data_after):
        temp = Node(data)
        self.data_after = data_after

        if self.head is None:
            self.head = temp
            return

        t = self.head

        while t.data is not data_after:
            t = t.next

        temp.next = t.next
        t.next.prev = temp

        t.next = temp
        temp.prev = t

    def InsertAtBegin(self, data):
        temp = Node(data)

        if self.head is None:
            self.head = temp
            return

        temp.next = self.head
        self.head.prev = temp
        self.head = temp

    def DeleteNode(self, data):
        if self.head is None:
            print("Linked list is empty!")
            return

        t = self.head

        if t.data == data:
            self.head = self.head.next
            self.head.prev = None
            return

        while t.next is not None:
            if t.data == data:
                t.prev.next = t.next
                t.next.prev = t.prev
                return

            t = t.next

        if t.data == data:
            t.prev.next = None

        
    def DisplayDLL(self):
        t = self.head

        while t is not None:
            print(t.data, end=" <-> ")
            t = t.next


obj = DoublyLinkedList()

obj.InsertAtEnd(10)
obj.InsertAtEnd(20)
obj.InsertAtEnd(30)
obj.InsertAtEnd(40)
obj.InsertAtEnd(50)

obj.InsertAtAnyPosition(400, 30)

obj.InsertAtBegin(5000)

obj.DeleteNode(5000)
obj.DisplayDLL()