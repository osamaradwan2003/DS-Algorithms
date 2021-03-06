from linked_list import LinkedList


class Stack(LinkedList):
    def __init__(self, *items):
        super().__init__()
        if(len(items) > 0):
            for i in items:
                self.append(i)

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
