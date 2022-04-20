from linked_list import LinkedList


class Stack(LinkedList):
    def __init__(self):
        super().__init__()

    def push(self, data):
        self.add(data=data)

    def pop(self):
        if(self.isEmpty()):
            raise RuntimeError("Empty Stack")
        return self.removeLast()

    def peek(self):
        if(self.isEmpty()):
            raise RuntimeError("Empty Stack")
        return self.getLast()

    def __iter__(self):
        return super().__iter__()

    def __next__(self):
        return super().__next__()
