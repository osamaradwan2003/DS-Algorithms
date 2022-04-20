from linked_list import LinkedList


class Queue(LinkedList):
    def __init__(self, *items):
        super().__init__()
        if(len(items) > 0):
            for i in items:
                self.append(i)

    def append(self, o: object):
        self.add(o)
        return self

    def shift(self):
        if(self.isEmpty()):
            raise RuntimeError("Empty Queue")
        return self.removeFirst()

    def peek(self):
        if(self.isEmpty()):
            raise RuntimeError("Empty Queue")
        return self.getFirst()

    def __iter__(self):
        return super().__iter__()

    def __next__(self):
        super().__next__()
