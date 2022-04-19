from node import Node


class LinkedList():

    # init linked list proparties
    def __init__(self):
        self.head = None
        self.tial = None
        self.size = 0

    # clear all Items in linked lists remove it from memory

    def clear(self):
        del self.head
        del self.tial
        self.size = 0
        self.head = None
        self.tial = None

    # allow len method to work with this class
    def __len__(self):
        return self.size

    # return empty status depended on size
    def isEmpty(self):
        return self.__len__() == 0

    # insert data to head or meke it first element

    def addFirst(self, data):
        if self.isEmpty():
            self.head = self.tial = Node(data)
        else:
            self.head.prev = Node(data, prev=None, next=self.head)
            self.head = self.head.prev
        self.size += 1

    # insert data on tail or mek it last element

    def addLast(self, data):
        if(self.isEmpty()):
            self.head = self.tial = Node(data)
        else:
            self.tial.next = Node(data, next=None, prev=self.tial)
            self.tial = self.tial.next
        self.size += 1

    # aials of  addLast Function
    def add(self, data):
        self.addLast(data)

    # get data value  from head
    def getFirst(self):
        if self.isEmpty():
            raise RuntimeError("List is Empty")
        return self.head.data

    # get data value from tail

    def getLast(self):
        if self.isEmpty():
            raise RuntimeError("List is Empty")
        return self.tial.data

    # remove first head and return it
    def removeFirst(self):
        if self.isEmpty():
            raise RuntimeError("List is Empty")
        data = self.head.data
        self.head = self.head.next
        self.size -= 1
        if(self.isEmpty()):
            self.tial = None
        self.head.prev = None
        return data

    # remove last tail and return it
    def removeLast(self):
        if self.isEmpty():
            raise RuntimeError("List is Empty")
        data = self.tial.data
        self.tial = self.tial.prev
        self.size -= 1
        if(self.isEmpty()):
            self.head = None
        self.tial.next = None
        return data

    # private method to remove items dependend on Node Object
    def __remove__(self, data: Node):
        if(data.prev == None):
            return self.removeFirst()
        if data.next == None:
            return self.removeLast()

        data.prev.next = data.next
        data.next.prev = data.prev
        alias = data.data
        del data
        self.size -= 1
        return alias

    # remove element by Index and return value
    def removeAt(self, index: int):
        if(index >= self.size or index < 0):
            raise IndexError()
        i = None
        trav = None
        # search from  front of the list
        if(index < self.size / 2):
            trav = self.head
            i = 0
            while i != index:
                trav = trav.next
                i += 1
        else:
            trav = self.tial
            i = self.size - 1
            while i != index:
                trav = trav.prev
                i -= 1
        return self.__remove__(trav)

    def remove(self, data: object) -> bool:
        """
          remove elemnt by vlaue and return status
          @return Bool ->  | True | False
        """
        trav = self.head
        while trav != None:
            if(trav.data == data):
                self.__remove__(trav)
                return True
            trav = trav.next
        return False

    def indexOf(self, data: object):
        trav = self.head
        i = 0
        while trav != None:
            if(trav.data == data):
                return i
            trav = trav.next
            i += 1
        return -1

    def contains(self, data: object):
        return self.indexOf(data) != -1

    def __iter__(self):
        self.trav = self.head
        return self

    def __next__(self):
        if(self.trav == None):
            raise StopIteration
        data = self.trav.data
        self.trav = self.trav.next
        return data

    def __str__(self) -> str:
        string = "["
        trav = self.head
        while trav != None:
            string += str(trav.data) + ","
            trav = trav.next
        string += "]"
        return string


# test linked list

# lists = LinkedList()

# lists.add(1)
# lists.add(2)
# lists.add(3)
# lists.add(4)
# lists.add(5)
# lists.add(6)
# lists.add(["ssss"])
# lists.add(8)
# lists.add(9)
# lists.add(10)

# print(lists)

# for i in lists:
#     print(i)
