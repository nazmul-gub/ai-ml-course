class Node: 
    def __init__(self, data):
        self.data = data
        self.next = None

class singly_linked_list: 
    def __init__(self, head = None): 
        self.head = head
        self.next = None

    def insertAtEnd(self, value):
        temp = Node(value)

        if self.head != None:
            t1 = self.head
            while(t1.next != None):
                t1 = t1.next
            t1.next = temp
        else:
            self.head = temp

    def insertAtBegining(self, value):
        temp = Node(value)

        temp.next = self.head
        self.head = temp

    def insertAtAnyPosition(self, value, position_after):
        temp = Node(value)

        t1 = self.head
        while(t1.next != None):
            if(t1.data == position_after):
                temp.next = t1.next
                t1.next = temp
            t1= t1.next


    def deleteValue(self, value):
        #empty list?
        if self.head is None:
            return

        #deleting the head node
        if self.head.data == value:
            self.head = self.head.next
            return

        #delete at any position

        prev = self.head
        current = self.head.next

        while current is not None:
            if current.data == value:
                prev.next = current.next
                return

            prev = current
            current = current.next
    

    def displayList(self): 
        t1 = self.head

        while(t1 != None):
            print(t1.data)
            t1 = t1.next

nazmul = singly_linked_list()

nazmul.insertAtEnd(10)
nazmul.insertAtEnd(20)
nazmul.insertAtEnd(30)
nazmul.insertAtEnd(40)

nazmul.insertAtBegining(100)

nazmul.insertAtAnyPosition(600,20)

nazmul.deleteValue(20)

nazmul.displayList()